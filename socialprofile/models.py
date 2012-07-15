"""Django Models for SocialProfile App"""

# pylint: disable=W0613, W0141

from django.db.models.signals import post_save
from social_auth.backends.facebook import FacebookBackend
from social_auth.backends.google import GoogleOAuth2Backend
from social_auth.backends.twitter import TwitterBackend
from django.db import models
from django.contrib.auth.models import User
from social_auth.signals import socialauth_registered, pre_update
from urllib import urlencode
from urllib2 import Request, urlopen
from django.utils import simplejson
from django.utils.translation import ugettext_lazy as _
import logging

LOGGER = logging.getLogger(name='socialprofile.models')

class SocialProfile(models.Model):
    """Main SocialProfile Object - Holds extra profile data retrieved from auth providers"""
    GENDER_CHOICES = (
        (_('male'), _('Male')),
        (_('female'), _('Female')),
        (_('other'), _('Other')),
        ('', '')
        )
    user = models.OneToOneField(User, related_name='social_profile', verbose_name=_("Social Profile"))
    gender = models.CharField(max_length=10, blank=True, choices=GENDER_CHOICES, verbose_name=_("Gender"))
    url = models.URLField(blank=True, verbose_name=_("Homepage"), help_text=_("Where can we find out more about you?"))
    image_url = models.URLField(blank=True, verbose_name=_("Avatar Picture"))
    description = models.TextField(blank=True, verbose_name=_("Description"), help_text=_("Tell us about yourself!"))

    class Meta:
        verbose_name = _("Social Profile")
        verbose_name_plural = _("Social Profiles")
        ordering = ['user__username']

    def __unicode__(self):
        return self.user.username

    @models.permalink
    def get_absolute_url(self):
        return 'sp_profile_other_view_page', [self.user.username]


def create_user_profile(sender, instance, created, **kwargs):
    """Creates a UserProfile Object Whenever a User Object is Created"""
    if created:
        SocialProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

def facebook_extra_values(sender, user, response, details, **kwargs):
    """Populates a UserProfile Object when a new User is created via Facebook Auth"""
    user.last_name = response.get('last_name', '')
    user.first_name = response.get('first_name', '')
    profile = user.social_profile
    profile.gender = response.get('gender', '')
    if response.get('username') is not None:
        profile.image_url = 'https://graph.facebook.com/' + response.get('username') + '/picture'
        profile.url = 'http://facebook.com/' + response.get('username')
    profile.url = response.get('link', '')
    if response.get('hometown') is not None:
        profile.description = response.get('hometown').get('name')

    profile.save()

    return True

socialauth_registered.connect(facebook_extra_values, sender=FacebookBackend)

def google_extra_values(sender, user, response, details, **kwargs):
    """Populates a UserProfile Object when a new User is created via Google Auth"""
    LOGGER.debug('socialprofile.models.google_extra_values')
    user_info_url = "https://www.googleapis.com/oauth2/v1/userinfo"

    data = {'access_token': response.get('access_token', ''), 'alt': 'json'}
    params = urlencode(data)
    try:
        request = Request(user_info_url + '?' + params, headers={'Authorization': params})
        result = simplejson.loads(urlopen(request).read())

        user.last_name = result.get('family_name', '')
        user.first_name = result.get('given_name', '')
        profile = user.social_profile
        profile.gender = result.get('gender', '')
        profile.image_url = result.get('picture', '')
        profile.url = result.get('link', '')

        profile.save()
    except:
        pass

    return True

socialauth_registered.connect(google_extra_values, sender=GoogleOAuth2Backend)

def twitter_extra_values(sender, user, response, details, **kwargs):
    """Populates a UserProfile Object when a new User is created via Twitter Auth"""
    try:
        first_name, last_name = response.get('name', '').split(' ', 1)
    except:
        first_name = response.get('name', '')
        last_name = ''
    user.last_name = last_name
    user.first_name = first_name
    profile = user.social_profile
    if response.get('screen_name') is not None:
        profile.url = 'http://twitter.com/' + response.get('screen_name', '')
    profile.image_url = response.get('profile_image_url_https', '')
    profile.description = response.get('description', '')

    profile.save()

    return True

socialauth_registered.connect(twitter_extra_values, sender=TwitterBackend)

def update_user_details(backend, details, response, user, is_new=False, *args,
                        **kwargs):
    """Override of social_auth method, to prevent details from getting updated."""
    LOGGER.debug("socialprofile.models.update_user_details")
    changed = False  # flag to track changes

    signal_response = lambda (receiver, response): response
    signal_kwargs = {'sender': backend.__class__, 'user': user,
                     'response': response, 'details': details}

    changed |= any(filter(signal_response, pre_update.send(**signal_kwargs)))

    # Fire socialauth_registered signal on new user registration
    if is_new:
        changed |= any(filter(signal_response,
            socialauth_registered.send(**signal_kwargs)))

    if changed:
        user.save()