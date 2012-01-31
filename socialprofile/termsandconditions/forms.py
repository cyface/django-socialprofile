"""Django forms for the termsandconditions application"""
from django import forms
from django.contrib.auth.models import User

import logging

logger = logging.getLogger(name='termsandconditions')

class TermsAndConditionsForm(forms.Form):
    """Master form for displaying and accepting Terms and Conditions"""
    # TODO: Build Acceptance Form
