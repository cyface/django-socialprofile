"""Unit Tests for the socialprofile module forms"""

# pylint: disable=R0904, C0103

from django.test import TestCase

from django.contrib.auth.models import User
from social.apps.django_app.default.models import UserSocialAuth
from socialprofile.forms import SocialProfileForm, UserForm
from django.forms.models import model_to_dict
import logging

LOGGER = logging.getLogger(name='socialprofile.test_forms')


class SocialProfileFormTestCase(TestCase):
    """Test Case for Social Profile Forms"""

    def setUp(self):
        """Set up common assets for tests"""
        LOGGER.debug("SocialProfileForm Tests setUp")
        self.user1 = User.objects.create_user('user1', 'user1@user1.com', 'user1password')
        self.user1.social_profile.gender = 'other'
        self.user1.social_profile.url = 'http://test.com'
        self.user1.social_profile.description = 'Test User 1'
        self.user1.social_profile.image_url = 'http://www.gravatar.com/avatar/00000000000000000000000000000000?d=mm'
        self.user1.save()
        self.sa1 = UserSocialAuth.objects.create(user=self.user1, provider='google-oauth2', uid='user1@user1.com')

    def test_socialprofile_form_view(self):
        """Test editing user profile data through form in isolation"""
        LOGGER.debug("Test socialprofile edit form")
        form = SocialProfileForm(instance=self.user1.social_profile)
        form_html = form.as_p()
        LOGGER.debug(form_html)
        self.assertInHTML('<option value="other" selected="selected">Other</option>', form_html)
        self.assertInHTML('<input id="id_returnTo" name="returnTo" type="hidden" value="/" />', form_html)
        self.assertInHTML('<textarea cols="40" id="id_description" name="description" rows="10">Test User 1</textarea>', form_html)
        self.assertInHTML('<input id="id_image_url" maxlength="500" name="image_url" type="url" value="http://www.gravatar.com/avatar/00000000000000000000000000000000?d=mm" />', form_html)
        self.assertInHTML('<input id="id_manually_edited" name="manually_edited" type="hidden" value="True" />', form_html)
        self.assertInHTML('<input id="id_url" maxlength="500" name="url" type="url" value="http://test.com" />', form_html)

    def test_socialprofile_form_update(self):
        LOGGER.debug("Test socialprofile edit form")
        data = model_to_dict(self.user1.social_profile)
        data['description'] = 'new description'
        data['gender'] = 'female'
        data['url'] = 'http://new.url'
        data['image_url'] = 'http://new.image.url'
        form = SocialProfileForm(data=data, instance=self.user1.social_profile)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEquals(self.user1.social_profile.description, 'new description')
        self.assertEquals(self.user1.social_profile.url, 'http://new.url')
        self.assertEquals(self.user1.social_profile.gender, 'female')
        self.assertEquals(self.user1.social_profile.image_url, 'http://new.image.url')

    def test_socialprofile_form_clean_desc(self):
        LOGGER.debug("Test socialprofile form clean desc")
        data = model_to_dict(self.user1.social_profile)
        data['description'] = '<a href="http://bad.url">Bad Link</a>'
        form = SocialProfileForm(data=data, instance=self.user1.social_profile)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEquals(self.user1.social_profile.description, 'Bad Link')


class UserFormTestCase(TestCase):
    """Tests for  User Form"""

    def setUp(self):
        """Set up common assets for tests"""
        LOGGER.debug("UserForm Tests setUp")
        self.user1 = User.objects.create_user('user1', 'user1@user1.com', 'user1password')

    def test_user_form_create(self):
        LOGGER.debug("Test user form create")
        data = {
            'username': 'user2',
            'password': 'user2password',
            'email': 'user@user2.com',
            'first_name': 'user',
            'last_name': '2',
            'last_login': '2012-09-04 06:00',
            'date_joined': '2012-09-04 06:00',
            'manually_edited': False
        }
        form = UserForm(data)
        self.assertTrue(form.is_valid())
        form.save()
        user2 = User.objects.get(username='user2')
        self.assertEquals(user2.username, 'user2')

    def test_user_form_view(self):
        """Test editing user profile data through form in isolation"""
        LOGGER.debug("Test user edit form")
        form = UserForm(instance=self.user1)
        form_html = form.as_p()
        LOGGER.debug(form_html)
        self.assertInHTML('<input id="id_username" maxlength="30" name="username" type="text" value="user1" />', form_html)
        self.assertInHTML('<input id="id_first_name" maxlength="30" name="first_name" type="text" />', form_html)
        self.assertInHTML('<input id="id_email" maxlength="254" name="email" type="email" value="user1@user1.com" />', form_html)
        self.assertInHTML('<input id="id_last_name" maxlength="30" name="last_name" type="text" />', form_html)
        self.assertNotIn('<input id="id_is_staff" name="is_staff" type="checkbox" />', form_html)
        self.assertNotIn('<input checked="checked" id="id_is_active" name="is_active" type="checkbox" />', form_html)

    def test_user_form_dupe_username(self):
        LOGGER.debug("Test user form update")
        data = {
            'username': 'user1',
            'password': 'user2password',
            'email': 'user@user2.com',
            'first_name': 'user',
            'last_name': '2',
            'last_login': '2012-09-04 06:00',
            'date_joined': '2012-09-04 06:00',
            'manually_edited': False
        }
        form = UserForm(data)
        self.assertIn('already exists', form.errors['username'][0])

    def test_user_form_update(self):
        LOGGER.debug("Test user form create")
        data = {
            'username': 'user1',
            'first_name': 'user',
            'last_name': 'Two',
            'last_login': '2012-09-04 06:00',
            'date_joined': '2012-09-04 06:00',
            'manually_edited': False
        }
        form = UserForm(data, instance=self.user1)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEquals(self.user1.last_name, 'Two')