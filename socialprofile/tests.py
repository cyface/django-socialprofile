"""Unit Tests for the socialprofile module"""

# pylint: disable=R0904, C0103

from django.test import TestCase

from django.contrib.auth.models import User
from socialprofile.models import SocialProfile
from social.apps.django_app.default.models import UserSocialAuth
import logging

LOGGER = logging.getLogger(name='socialprofile')


class SocialProfileTestCase(TestCase):
    """Test Case for Social Profile"""

    def setUp(self):
        """Set up common assets for tests"""
        LOGGER.debug("SocialProfile Tests setUp")
        self.user1 = User.objects.create_user('user1', 'user1@user1.com', 'user1password')
        self.sp1 = SocialProfile.objects.update(user=self.user1,
                                                gender="Male",
                                                url="http://test.com",
                                                description="Test User 1",
                                                image_url="http://www.gravatar.com/avatar/00000000000000000000000000000000?d=mm"
        )
        self.sa1 = UserSocialAuth.objects.create(user=self.user1, provider='google-oauth2', uid='user1@user1.com')
        self.sa2 = UserSocialAuth.objects.create(user=self.user1, provider='facebook', uid='user1@user1.com')
        self.sa2 = UserSocialAuth.objects.create(user=self.user1, provider='twitter', uid='user1@user1.com')

    def tearDown(self):
        """Remove Test Data"""
        LOGGER.debug("SocialProfile Tests tearDown")
        self.user1.delete()

    def test_redirect_urls(self):
        """Test that redirects kicking in when trying to go to secure page."""
        LOGGER.debug("SocialProfile Test Redirect URLs")
        response = self.client.get('/secure/', follow=True)
        self.assertRedirects(response, "http://testserver/socialprofile/select/?next=/secure/")

    def test_view_profile(self):
        """Test to see if profile for user1 can be viewed anon and logged in"""
        LOGGER.debug("Test GET /socialprofile/view/user1/ for anon user")
        anon_view_response = self.client.get('/socialprofile/view/user1/')
        self.assertContains(anon_view_response, "Test User 1")

        LOGGER.debug("Test GET /socialprofile/ for anon user")
        anon_view_generic_response = self.client.get('/socialprofile/')
        self.assertEqual(404, anon_view_generic_response.status_code)

        LOGGER.debug("Test GET /socialprofile/view/ for anon user")
        anon_view_generic_response_2 = self.client.get('/socialprofile/view/')
        self.assertEqual(404, anon_view_generic_response_2.status_code)

        LOGGER.debug("Test GET /socialprofile/view/user1/ for logged in user")
        self.client.login(username='user1', password='user1password')
        logged_in_view_response = self.client.get('/socialprofile/view/user1/')
        self.assertContains(logged_in_view_response, "Test User 1")

        LOGGER.debug("Test GET /socialprofile/ for logged in user")
        logged_in_view_generic_response = self.client.get('/socialprofile/')
        self.assertContains(logged_in_view_generic_response, "Test User 1")

        LOGGER.debug("Test GET /socialprofile/view/ for logged in user")
        logged_in_view_generic_response_2 = self.client.get('/socialprofile/view/')
        self.assertEqual(404, logged_in_view_generic_response_2.status_code)

        LOGGER.debug("Test GET /socialprofile/view/ for logged in user")
        logged_in_view_generic_response_2 = self.client.get('/socialprofile/view/')
        self.assertEqual(404, logged_in_view_generic_response_2.status_code)

        LOGGER.debug("Test POST to /socialprofile/view/ for logged in user")
        logged_in_view_post_response = self.client.post('/socialprofile/', {'user': 1}, follow=True)
        self.assertEqual(405, logged_in_view_post_response.status_code)  # HTTP POST Not Allowed

    def test_socialprofile_permalink(self):
        """Test the permalink method of SocialProfile"""
        LOGGER.debug("Test SocialProfile Permalink")
        profile = SocialProfile.objects.get(user=self.user1)
        permalink = profile.get_absolute_url()
        self.assertEqual("/socialprofile/view/user1/", permalink)
        anon_view_response = self.client.get(permalink)
        self.assertContains(anon_view_response, "Test User 1")

    def test_edit_profile(self):
        """Test to see if profile for user1 can be edited anon and logged in"""
        LOGGER.debug("Test GET /socialprofile/edit/user1/ for anon user")
        anon_edit_response = self.client.get('/socialprofile/edit/user1/')
        self.assertEqual(404, anon_edit_response.status_code)

        LOGGER.debug("Test GET /socialprofile/edit/ for anon user")
        anon_edit_response_2 = self.client.get('/socialprofile/edit/')
        self.assertRedirects(anon_edit_response_2, "http://testserver/socialprofile/select/?next=/socialprofile/edit/")

        LOGGER.debug("Test POST /socialprofile/edit/ for anon user")
        anon_edit_response_2 = self.client.post('/socialprofile/edit/', {'user': 1}, follow=True)
        self.assertRedirects(anon_edit_response_2, "http://testserver/socialprofile/select/?next=/socialprofile/edit/")

        LOGGER.debug("Test GET /socialprofile/edit/user1/ for logged in user")
        self.client.login(username='user1', password='user1password')
        anon_edit_response = self.client.get('/socialprofile/edit/user1/')
        self.assertEqual(404, anon_edit_response.status_code)

        LOGGER.debug("Test GET /socialprofile/edit/ for logged in user")
        logged_in_edit_response = self.client.get('/socialprofile/edit/')
        self.assertContains(logged_in_edit_response, "Test User 1")

        LOGGER.debug("Test POST /socialprofile/edit/ for logged in user")
        post_data = {
            'user': 1,
            'username': 'user2',
            'email': 'user1@test.com',
            'first_name': 'Test',
            'last_name': 'User',
            'description': "Test1 User",
            'image_url': 'http://foo.com',
            'url': 'http://user1.com',
            'returnTo': '/secure/'
        }
        logged_in_edit_response_2 = self.client.post('/socialprofile/edit/', post_data, follow=True)
        self.assertContains(logged_in_edit_response_2, "updated")
        user = User.objects.get(username='user2')
        self.assertEqual('user2', str(user.social_profile))

        LOGGER.debug("Test Invalid Form Error")
        post_data = {
            'username': 'user2',
            'email': 'user1@test.com',
            'gender': 'Robot',
            'first_name': 'Test',
            'last_name': 'User',
            'description': "Test1 User",
            'image_url': 'http://foo.com',
            'url': 'http://user1.com',
            'returnTo': '/secure/'
        }
        logged_in_edit_response_3 = self.client.post('/socialprofile/edit/', post_data, follow=True)
        self.assertContains(logged_in_edit_response_3, "NOT")


    def test_delete_user(self):
        """Test the views that enable deleting users/socialprofiles"""
        LOGGER.debug("Test GET /socialprofile/delete/ for logged in user")
        self.client.login(username='user1', password='user1password')
        logged_in_delete_response = self.client.get('/socialprofile/delete/')
        self.assertContains(logged_in_delete_response, "Really Delete")

        LOGGER.debug("Test POST to /socialprofile/delete/ for logged in user")
        logged_in_delete_post_response = self.client.post('/socialprofile/delete/', {'user': 1}, follow=True)
        self.assertRedirects(logged_in_delete_post_response, '/')

        LOGGER.debug("Test GET /socialprofile/view/user1/ for deleted user")
        deleted_response = self.client.get('/socialprofile/view/user1/')
        # LOGGER.debug(deleted_response)
        self.assertEqual(404, deleted_response.status_code)





