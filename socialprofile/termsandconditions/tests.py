"""Unit Tests for the socialprofile module"""

# pylint: disable=R0904

import unittest
from django.contrib.auth.models import User
from termsandconditions.models import TermsAndConditions
from termsandconditions.models import UserTermsAndConditions

class TermsAndConditionsTests(unittest.TestCase):
    """Tests Terms and Conditions Module"""
    def setUp(self):
        """Setup for each test"""
        self.user1 = User.objects.create(username='user1')
        self.user2 = User.objects.create(username='user2')
        self.terms1 = TermsAndConditions.objects.create(text="Terms and Conditions1", version_number=1.0)
        self.terms2 = TermsAndConditions.objects.create(text="Terms and Conditions2", version_number=2.0)

    def test_accept_terms(self):
        """Accept Terms"""
        UserTermsAndConditions.objects.create(user=self.user1, terms=self.terms1)
        UserTermsAndConditions.objects.create(user=self.user2, terms=self.terms2)

        self.assertEquals(1.0, self.user1.usertermsandconditions.terms.version_number)
        self.assertEquals(2.0, self.user2.usertermsandconditions.terms.version_number)

