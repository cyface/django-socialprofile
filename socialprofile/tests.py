import unittest
from urllib import urlencode
from urllib2 import Request, urlopen
from django.utils import simplejson

class OauthGoogleTestCase(unittest.TestCase):
    def testGetUserData(self):
        access_token = 'GETAFRESHONE'

        user_info_url = "https://www.googleapis.com/oauth2/v1/userinfo"

        data = {'access_token': access_token, 'alt': 'json'}
        params = urlencode (data)
        request = Request(user_info_url + '?' + params, headers={'Authorization': params})
        result =  simplejson.loads(urlopen(request).read())

        print result

        print result['family_name']

