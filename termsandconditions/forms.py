"""Django forms for the termsandconditions application"""
from django import forms
from django.contrib.auth.models import User
from termsandconditions.models import TermsAndConditions

import logging

logger = logging.getLogger(name='termsandconditions')

class TermsAndConditionsForm(forms.Form):
    """Master form for displaying and accepting Terms and Conditions"""
    text = forms.CharField(widget=forms.Textarea(attrs={'readonly':'readonly', 'class':'terms-text'}))
    slug = forms.SlugField(widget=forms.HiddenInput)

    def __init__(self, data=None, slug='default', initial=None, *args, **kwargs):
        """Lets you pass in a user= to bind this form from"""
        if initial is None:
            terms = TermsAndConditions.get_active(slug)
            text = terms.text
            slug = terms.slug

            initial = dict(text=text, slug=slug)

        super(TermsAndConditionsForm, self).__init__(data=data, initial=initial, *args, **kwargs)
