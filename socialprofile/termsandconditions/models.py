"""Django Models for TermsAndConditions App"""

# pylint: disable=W0613

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
import datetime
import logging

log = logging.getLogger(name='termsandconditions')

if hasattr(settings, 'DEFAULT_TERMS_SLUG'):
    DEFAULT_TERMS_SLUG = settings.DEFAULT_TERMS_SLUG
else:
    DEFAULT_TERMS_SLUG = 'site-terms'

class UserTermsAndConditions(models.Model):
    """Holds mapping between TermsAndConditions and Users"""
    user = models.OneToOneField(User, related_name="userterms")
    terms = models.OneToOneField("TermsAndConditions", related_name="terms")
    ip_address = models.IPAddressField(null=True, blank=True)
    date_accepted = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'date_accepted'

class TermsAndConditions(models.Model):
    """Holds Versions of TermsAndConditions
    Active one for a given slug is: date_active is not Null and is latest not in future"""
    slug = models.SlugField(default='site-terms')
    name = models.TextField(max_length=255)
    users = models.ManyToManyField(User, through=UserTermsAndConditions, blank=True, null=True,)
    version_number = models.DecimalField(default=1.0, decimal_places=2, max_digits=6)
    text = models.TextField(null=True, blank=True)
    date_active = models.DateTimeField(blank=True, null=True, help_text="Leave Null To Never Make Active")
    date_created = models.DateTimeField(blank=True, auto_now_add=True)

    class Meta:
        ordering = ['-date_active',]
        get_latest_by = 'date_active'
        verbose_name_plural = 'Terms and Conditions'

    @staticmethod
    def get_active(slug='default'):
        """Finds the latest of a particular terms and conditions"""
        if slug == 'default':
            slug = DEFAULT_TERMS_SLUG

        return TermsAndConditions.objects.filter(date_active__isnull=False, date_active__lte=datetime.datetime.now(), slug=slug).latest('date_active')

    @staticmethod
    def agreed_to_latest(user, slug='default'):
        """Checks to see if a specified user has agreed to the latest of a particular terms and conditions"""
        if slug == 'default':
            slug = DEFAULT_TERMS_SLUG
        try:
            UserTermsAndConditions.objects.get(user=user, terms=TermsAndConditions.get_active(slug))

            return True
        except UserTermsAndConditions.DoesNotExist:
            return False