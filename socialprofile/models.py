"""Django Models for SocialProfile App"""

# pylint: disable=C0111,E0202,W0613,W0141

from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User
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

    class Meta(object):
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



#
#
# socialauth_registered.connect(twitter_extra_values, sender=TwitterBackend)
#
#
# def update_user_details(backend, details, response, user, is_new=False, *args,
# **kwargs):
# """Override of social_auth method, to prevent details from getting updated."""
#     LOGGER.debug("socialprofile.models.update_user_details")
#     changed = False  # flag to track changes
#
#     signal_response = lambda (receiver, response): response
#     signal_kwargs = {'sender': backend.__class__, 'user': user,
#                      'response': response, 'details': details}
#
#     changed |= any(filter(signal_response, pre_update.send(**signal_kwargs)))
#
#     # Fire socialauth_registered signal on new user registration
#     if is_new:
#         changed |= any(filter(signal_response,
#                               socialauth_registered.send(**signal_kwargs)))
#
#     if changed:
#         user.save()
