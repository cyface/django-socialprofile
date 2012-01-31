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
        self.terms1 = TermsAndConditions.objects.create(slug="siteterms", name="Site Terms", text="Terms and Conditions1", version_number=1.0, date_active="2012-01-01")
        self.terms2 = TermsAndConditions.objects.create(slug="siteterms", name="Site Terms", text="Terms and Conditions2", version_number=2.0, date_active="2012-01-05")
        self.terms3 = TermsAndConditions.objects.create(slug="contribterms", name="Contributor Terms", text="Terms and Conditions1", version_number=1.5, date_active="2012-01-01")
        self.terms4 = TermsAndConditions.objects.create(slug="contribterms", name="Contributor Terms", text="Terms and Conditions1", version_number=2.0, date_active="2100-01-01")


    def test_terms_and_conditions(self):
        """Various tests of the TermsAndConditions Module"""

        """Testing Direct Assignment of Acceptance"""
        UserTermsAndConditions.objects.create(user=self.user1, terms=self.terms1)
        UserTermsAndConditions.objects.create(user=self.user2, terms=self.terms3)

        self.assertEquals(1.0, self.user1.userterms.terms.version_number)
        self.assertEquals(1.5, self.user2.userterms.terms.version_number)

        self.assertEquals('user1', self.terms1.users.all()[0].username)

        """Testing the get_active static method of TermsAndConditions"""
        self.assertEquals(2.0, TermsAndConditions.get_active(slug='siteterms').version_number)
        self.assertEquals(1.5, TermsAndConditions.get_active(slug='contribterms').version_number)

        """Testing the agreed_to_latest static method of TermsAndConditions"""
        self.assertEquals(False, TermsAndConditions.agreed_to_latest(user=self.user1, slug='siteterms'))
        self.assertEquals(True, TermsAndConditions.agreed_to_latest(user=self.user2, slug='contribterms'))

