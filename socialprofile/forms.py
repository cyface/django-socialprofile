"""Django forms for the socialprofile application"""
from django import forms
from django.contrib.auth.models import User
from .models import SocialProfile
from django.utils.html import strip_tags
import logging

# pylint: disable=E1120,W0212

LOGGER = logging.getLogger(name='socialprofile.forms')


class UserForm(forms.ModelForm):
    """Form for editing the data that is part of the User model"""

    class Meta(object):
        """Configuration for the ModelForm"""
        model = User
        fields = {'username', 'first_name', 'last_name', 'email'}


class SocialProfileForm(forms.ModelForm):
    """Master form for editing the user's profile"""

    user = forms.IntegerField(widget=forms.HiddenInput, required=True)
    returnTo = forms.CharField(widget=forms.HiddenInput, required=False, initial='/')  # URI to Return to after save
    manually_edited = forms.BooleanField(widget=forms.HiddenInput, required=False, initial=True)

    class Meta(object):
        """Configuration for the ModelForm"""
        model = SocialProfile
        fields = {'user', 'gender', 'url', 'image_url', 'description'}  # Don't let through for security reasons, user should be based on logged in user only

    def clean_description(self):
        """Automatically called by Django, this method 'cleans' the description, e.g. stripping HTML out of desc"""

        LOGGER.debug("socialprofile.forms.SocialProfileForm.clean_description")

        return strip_tags(self.cleaned_data['description'])

    def clean(self):
        """Automatically called by Django, this method 'cleans' the whole form"""

        LOGGER.debug("socialprofile.forms.SocialProfileForm.clean")

        if self.changed_data:
            self.cleaned_data['manually_edited'] = True
