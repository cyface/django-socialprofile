"""Django forms for the termsandconditions application"""
from django import forms
from django.contrib.auth.models import User
from termsandconditions.models import TermsAndConditions

import logging

logger = logging.getLogger(name='termsandconditions')

class TermsAndConditionsForm(forms.Form):
    """Master form for displaying and accepting Terms and Conditions"""
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, data=None, slug=None, initial=None, *args, **kwargs):
        """Lets you pass in a user= to bind this form from"""
        if initial is None:
            text = TermsAndConditions.get_active(slug).text

            initial = dict(text=text)

        super(TermsAndConditionsForm, self).__init__(data=data, initial=initial, *args, **kwargs)
