"""Django forms for the socialprofile application"""
from django import forms
from django.contrib.auth.models import User
from models import SocialProfile
from django.core.exceptions import ObjectDoesNotExist
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _
from widgets import H5EmailInput
import logging

LOGGER = logging.getLogger(name='socialprofile')

class SocialProfileForm(forms.ModelForm):
    """Master form for editing the user's profile"""

    username = forms.CharField(max_length=30, label='User Name')
    email = forms.EmailField(label="Email Address", widget=H5EmailInput())
    first_name = forms.CharField(max_length=30, required=False, label='First Name', )
    last_name = forms.CharField(max_length=30, required=False, label='Last Name')
    returnTo = forms.CharField(widget=forms.HiddenInput, required=False, initial='/') #URI to Return to after save

    class Meta():
        """Configuration for the ModelForm"""
        model = SocialProfile
        exclude = {'user'} #Don't let through for security reasons, user should be based on logged in user only

    def clean_description(self):
        """Automatically called by Django, this method 'cleans' the description, in our case stripping HTML out of description"""

        LOGGER.debug("socialprofile.forms.SocialProfileForm.clean_description")

        return strip_tags(self.cleaned_data['description'])

    def clean(self):
        """Automatically called by Django, this method 'cleans' the whole form"""

        LOGGER.debug("socialprofile.forms.SocialProfileForm.clean")

        changed_data = self.changed_data

        user_field_objects = User._meta.fields

        user_fields = []
        for field_object in user_field_objects:
            user_fields.append(field_object.name)

        user_dirty = False

        for changed_field in changed_data:
            if changed_field in user_fields:
                user_dirty = True
                setattr(self.instance.user, changed_field, self.cleaned_data.get(changed_field))

            if changed_field == 'username': # Check Username for Uniqueness
                try:
                    User.objects.get(username=self.cleaned_data.get('username'))
                    raise forms.ValidationError([_("Your new username is not available!")])
                except ObjectDoesNotExist:
                    pass # good news, the new username is available

            if user_dirty:
                self.instance.user.save()

        return self.cleaned_data