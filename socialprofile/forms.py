"""Django forms for the socialprofile application"""
from django import forms
from django.contrib.auth.models import User
from models import SocialProfile
from django.core.exceptions import ObjectDoesNotExist
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _
from widgets import H5EmailInput
import logging

# pylint: disable=E1120,W0212

LOGGER = logging.getLogger(name='socialprofile.forms')


class UserForm(forms.ModelForm):
    """Form for editing the data that is part of the User model"""

    class Meta(object):
        """Configuration for the ModelForm"""
        model = User
        fields = {'username', 'first_name', 'last_name', 'email'}

    def clean(self):
        """Automatically called by Django, this method 'cleans' the whole form"""

        LOGGER.debug("socialprofile.forms.UserForm.clean")

        for changed_field in self.changed_data:
            user_dirty = True

            if changed_field == 'username':  # Check Username for Uniqueness
                try:
                    User.objects.get(username=self.cleaned_data.get('username'))
                    raise forms.ValidationError([_("Your new username is not available!")])
                except ObjectDoesNotExist:
                    pass  # good news, the new username is available

            if user_dirty:
                self.cleaned_data['manually_edited'] = True

        return self.cleaned_data


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


