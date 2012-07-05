"""Unit Tests for the socialprofile module"""

# pylint: disable=R0904, C0103

from django.test import TestCase

from django.test.client import Client

#from urllib import urlencode
#from urllib2 import Request, urlopen
#from django.utils import simplejson
#class OauthGoogleTestCase(unittest.TestCase):
#    """Tests Google Oauth for extra values, you need to look in user_auth tables for an access_token"""
#    def testGetUserData(self):
#        """Test user data from Google oauth"""
#        access_token = 'GETAFRESHONE'
#
#        user_info_url = "https://www.googleapis.com/oauth2/v1/userinfo"
#
#        data = {'access_token': access_token, 'alt': 'json'}
#        params = urlencode (data)
#        request = Request(user_info_url + '?' + params, headers={'Authorization': params})
#        result =  simplejson.loads(urlopen(request).read())
#
#        print result
#
#        print result['family_name']

class SocialProfileUrlsTestCase(TestCase):
    """Test Case for Social Profile URLs"""

    def setUp(self):
        """Set up common assets for tests"""
        self.c = Client()

    def test_redirect_urls(self):
        """Test that redirects kicking in when trying to go to secure page."""
        response = self.c.get('/secure/', follow=True)
        self.assertRedirects(response, "http://testserver/socialprofile/select/?next=/secure/")
