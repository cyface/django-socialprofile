"""Django Models for TermsAndConditions App"""

# pylint: disable=W0613

from django.contrib.auth.models import User
from django.db import models
import logging

log = logging.getLogger(name='termsandconditions')

class UserTermsAndConditions(models.Model):
    """Holds mapping between TermsAndConditions and Users"""
    user = models.OneToOneField(User)
    terms = models.OneToOneField("TermsAndConditions", related_name="terms")
    ip_address = models.DecimalField(null=True, decimal_places=2, max_digits=6)
    date_accepted = models.DateTimeField(auto_now_add=True)

class TermsAndConditions(models.Model):
    """Holds Versions of TermsAndConditions"""
    usertermsandconditions = models.ManyToManyField(User, through=UserTermsAndConditions)
    version_number = models.DecimalField(default=1.0, decimal_places=2, max_digits=6)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)