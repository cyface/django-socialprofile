"""Unit Tests for the socialprofile module forms"""

# pylint: disable=R0904, C0103

from django.test import TestCase

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from socialprofile.models import SocialProfile
from social.apps.django_app.default.models import UserSocialAuth
from socialprofile.forms import SocialProfileForm, UserForm
from django.forms.models import model_to_dict
from socialprofile.pipeline import facebook_extra_values, google_extra_values, socialprofile_extra_values, twitter_extra_values
from social.backends.google import GoogleOAuth2
from social.backends.twitter import TwitterOAuth
from social.backends.facebook import Facebook2OAuth2

import logging

LOGGER = logging.getLogger(name='socialprofile.test_forms')


class SocialProfilePipelineTestCase(TestCase):
    """Test Case for Social Profile Pipeline"""

    def setUp(self):
        """Set up common assets for tests"""
        LOGGER.debug("SocialProfile Pipeline Tests setUp")
        self.user1 = User.objects.create_user('user1', 'user1@user1.com', 'user1password')
        self.user1.social_profile.gender = 'other'
        self.user1.social_profile.url = 'http://test.com'
        self.user1.social_profile.description = 'Test User 1'
        self.user1.social_profile.image_url = 'http://www.gravatar.com/avatar/00000000000000000000000000000000?d=mm'
        self.user1.save()
        self.sa1 = UserSocialAuth.objects.create(user=self.user1, provider='google-oauth2', uid='user1@user1.com')

    def test_socialprofile_pipeline_google(self):
        """Test editing executing pipeline methods in isolation for google"""
        LOGGER.debug("Test socialprofile pipeline Google")
        backend = GoogleOAuth2()
        response = {
            'name': {
                'familyName': 'User 1',
                'givenName': 'Test'
            },
            'gender': 'other',
            'image': {'url': 'http://image.url'},
            'occupation': 'User Description',
            'url': 'http://test.com'
        }

        socialprofile_extra_values(backend, {}, response, '1', self.user1)
        self.assertEquals(self.user1.social_profile.description, 'User Description')
        self.assertEquals(self.user1.social_profile.gender, 'other')
        self.assertEquals(self.user1.social_profile.image_url, 'http://image.url')
        self.assertEquals(self.user1.social_profile.url, 'http://test.com')

    def test_socialprofile_pipeline_facebook(self):
        """Test editing executing pipeline methods in isolation for facebook"""
        LOGGER.debug("Test socialprofile pipeline Facebook")
        backend = Facebook2OAuth2()
        response = {
            'name': {
                'last_name': 'User 1',
                'first_name': 'Test'
            },
            'gender': 'other',
            'picture': {'data': {'url': 'http://image.url'}},
            'link': 'http://test.com'
        }

        socialprofile_extra_values(backend, {}, response, '1', self.user1)
        self.assertEquals(self.user1.social_profile.gender, 'other')
        self.assertEquals(self.user1.social_profile.image_url, 'http://image.url')
        self.assertEquals(self.user1.social_profile.url, 'http://test.com')

    def test_socialprofile_pipeline_twitter(self):
        """Test editing executing pipeline methods in isolation for twitter"""
        LOGGER.debug("Test socialprofile pipeline Twitter")
        backend = TwitterOAuth()
        response = {
            'name': {
                'last_name': 'User 1',
                'first_name': 'Test'
            },
            'gender': 'other',
            'profile_image_url_https': 'http://image.url',
            'description': 'User Description',
            'url': 'http://test.com'
        }

        socialprofile_extra_values(backend, {}, response, '1', self.user1)
        self.assertEquals(self.user1.social_profile.description, 'User Description')
        self.assertEquals(self.user1.social_profile.gender, 'other')
        self.assertEquals(self.user1.social_profile.image_url, 'http://image.url')
        self.assertEquals(self.user1.social_profile.url, 'http://test.com')