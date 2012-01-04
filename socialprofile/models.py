from django.db.models.signals import post_save
from social_auth.backends.facebook import FacebookBackend
from social_auth.backends.google import GoogleOAuth2Backend
from social_auth.backends.twitter import TwitterBackend
from django.db import models
from django.contrib.auth.models import User
from social_auth.signals import socialauth_registered
from urllib import urlencode
from urllib2 import Request, urlopen
from django.utils import simplejson
import logging

log = logging.getLogger(name='socialprofile')

class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ('', '')
        )
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=10, blank=True, choices=GENDER_CHOICES)
    url = models.URLField(blank=True)
    image_url = models.URLField(blank=True)
    description = models.TextField(blank=True)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

def facebook_extra_values(sender, user, response, details, **kwargs):
    user.last_name = response['last_name']
    user.first_name = response['first_name']
    profile = user.get_profile()
    profile.gender = response['gender']
    profile.image_url = 'https://graph.facebook.com/' + response['username'] + '/picture'
    profile.url = response['link']
    if response['hometown']:
        profile.description = response['hometown']['name']

    profile.save()

    return True

socialauth_registered.connect(facebook_extra_values, sender=FacebookBackend)

def google_extra_values(sender, user, response, details, **kwargs):
#    log.debug('Inside Google Extra Values Handler')
    user_info_url = "https://www.googleapis.com/oauth2/v1/userinfo"

    data = {'access_token': response['access_token'], 'alt': 'json'}
    params = urlencode (data)
    request = Request(user_info_url + '?' + params, headers={'Authorization': params})
    result =  simplejson.loads(urlopen(request).read())

    user.last_name = result['family_name']
    user.first_name = result['given_name']
    profile = user.get_profile()
    profile.gender = result['gender']
    profile.image_url = result['picture']
    profile.url = result['link']

    profile.save()

    return True

socialauth_registered.connect(google_extra_values, sender=GoogleOAuth2Backend)

def twitter_extra_values(sender, user, response, details, **kwargs):
    try:
        first_name, last_name = response['name'].split(' ', 1)
    except:
        first_name = response['name']
        last_name = ''
    user.last_name = last_name
    user.first_name = first_name
    profile = user.get_profile()
    profile.url = 'http://twitter.com/' + response.get('screen_name', '')
    profile.image_url = response.get('profile_image_url_https', '')
    profile.description = response.get('description', '')

    profile.save()

    return True

socialauth_registered.connect(twitter_extra_values, sender=TwitterBackend)