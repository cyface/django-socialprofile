"""Django forms for the socialprofile application"""
from django import forms
from django.contrib.auth.models import User
from models import SocialProfile
from django.core.exceptions import ObjectDoesNotExist
from django.utils.html import strip_tags
from django.forms.models import model_to_dict
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

        working_username = self.cleaned_data.get('username')

        # Check Username for Uniqueness
        try:
            existingUser = User.objects.get(username=working_username)
        except ObjectDoesNotExist:
            existingUser = None

        if existingUser is not None and self.instance.user is not None:
            if self.instance.user.id != existingUser.id:
                raise forms.ValidationError([u"Your new username is not unique!"])

        user_dirty = False
        if self.instance.user.username != self.cleaned_data.get('username'): user_dirty = True
        if self.instance.user.email != self.cleaned_data.get('email'): user_dirty = True
        if self.instance.user.first_name != self.cleaned_data.get('first_name'): user_dirty = True
        if self.instance.user.last_name != self.cleaned_data.get('last_name'): user_dirty = True

        if user_dirty:
            self.instance.user.username = self.cleaned_data.get('username')
            self.instance.user.email = self.cleaned_data.get('email')
            self.instance.user.first_name = self.cleaned_data.get('first_name')
            self.instance.user.last_name = self.cleaned_data.get('last_name')
            self.instance.user.save()

        return self.cleaned_data

#    def __init__(self, *args, **kwargs):
#        if hasattr(self, 'user') and self.username:
#            LOGGER.debug ('HAVE NO USER, BUT DO HAVE USERNAME')
#        super(SocialProfileForm, self).__init__(args, kwargs)
