"""Python Social Auth Pipeline Extensions"""

from urllib import urlencode
from urllib2 import Request, urlopen
import json
from social.backends.google import GoogleOAuth2
from social.backends.twitter import TwitterOAuth

import logging

LOGGER = logging.getLogger(name='socialprofile.models')


def socialprofile_extra_values(backend, details, response, uid, user, *args, **kwargs):
    """Routes the extra values call to the appropriate back end"""
    if type(backend) is GoogleOAuth2:
        google_extra_values(backend, details, response, uid, user, *args, **kwargs)

    if type(backend) is TwitterOAuth:
        twitter_extra_values(backend, details, response, uid, user, *args, **kwargs)


def google_extra_values(backend, details, response, uid, user, *args, **kwargs):
    """Populates a UserProfile Object when a new User is created via Google Auth"""
    LOGGER.debug('socialprofile.pipeline.google_extra_values')
    user_info_url = "https://www.googleapis.com/oauth2/v1/userinfo"

    data = {'access_token': response.get('access_token', ''), 'alt': 'json'}
    params = urlencode(data)
    try:
        request = Request(user_info_url + '?' + params, headers={'Authorization': params})
        result = json.loads(urlopen(request).read())

        user.last_name = result.get('family_name', '')
        user.first_name = result.get('given_name', '')
        profile = user.social_profile
        profile.gender = result.get('gender', '')
        profile.image_url = result.get('picture', '')
        profile.url = result.get('link', '')

        profile.save()
    except:
        pass

    return response


# def facebook_extra_values(sender, user, response, details, **kwargs):
# """Populates a UserProfile Object when a new User is created via Facebook Auth"""
# user.last_name = response.get('last_name', '')
#     user.first_name = response.get('first_name', '')
#     profile = user.social_profile
#     profile.gender = response.get('gender', '')
#     if response.get('username') is not None:
#         profile.image_url = 'https://graph.facebook.com/' + response.get('username') + '/picture'
#         profile.url = 'http://facebook.com/' + response.get('username')
#     profile.url = response.get('link', '')
#     if response.get('hometown') is not None:
#         profile.description = response.get('hometown').get('name')
#
#     profile.save()
#
#     return True
#
#
# socialauth_registered.connect(facebook_extra_values, sender=FacebookBackend)

def twitter_extra_values(backend, details, response, uid, user, *args, **kwargs):
    """Populates a UserProfile Object when a new User is created via Twitter Auth"""
    LOGGER.debug('socialprofile.pipeline.twitter_extra_values')
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