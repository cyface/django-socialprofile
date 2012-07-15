"""Django Views for the socialprofile module"""

# pylint: disable=R0901

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import Http404
from django.views.generic import TemplateView, FormView, UpdateView, DeleteView
from models import SocialProfile
from django.forms.models import model_to_dict
from django.utils.translation import ugettext_lazy as _

from forms import SocialProfileForm

import logging

LOGGER = logging.getLogger(name='socialprofile')

DEFAULT_RETURNTO_PATH = getattr(settings, 'DEFAULT_RETURNTO_PATH', '/')

class SelectAuthView(TemplateView):
    """
    Lets users choose how they want to request access.

    url: /select
    """
    template_name = 'socialprofile/sp_account_select.html'

    def get_context_data(self, **kwargs):
        """Ensure that 'next' gets passed along"""
        LOGGER.debug('socialprofile.views.SelectAuthView.get_context_data')

        nextPage = self.request.GET.get(REDIRECT_FIELD_NAME, DEFAULT_RETURNTO_PATH)

        context = super(SelectAuthView, self).get_context_data(**kwargs)
        context['next_param'] = REDIRECT_FIELD_NAME
        context['next_url'] = nextPage
        return context


class SocialProfileView(FormView):
    """
    Profile View Page

    url: /profile/view
    """
    template_name = 'socialprofile/sp_profile_view.html'

    form_class = SocialProfileForm

    http_method_names = ['get'] #Limit to get for security reasons

    def get_initial(self):
        """Load up the default data to show in the display form."""
        LOGGER.debug("socialprofile.views.SocialProfileView.get_initial")
        username = self.kwargs.get('username')
        if username:
            user = get_object_or_404(User, username=username)
        elif self.request.user.is_authenticated():
            user = self.request.user
        else:
            raise Http404 #Case where user gets to this view anonymously for non-existent user

        returnTo = self.request.GET.get('returnTo', DEFAULT_RETURNTO_PATH)

        social_profile = SocialProfile.objects.get(user=user)

        self.object = social_profile

        initial_data = model_to_dict(social_profile)
        initial_data.update(model_to_dict(user))
        initial_data.update({'returnTo': returnTo})

        return initial_data


class SocialProfileEditView(UpdateView):
    """
    Profile Editing View

    url: /profile/edit
    """

    template_name = 'socialprofile/sp_profile_edit.html'

    form_class = SocialProfileForm

    model = SocialProfile

    def get_object(self, queryset=None):
        return SocialProfile.objects.get(user=self.request.user) #Force get from current user for security

    def get_initial(self):
        """Load up the default data to show in the form."""
        LOGGER.debug("socialprofile.views.SocialProfileEditView.get_initial")

        returnTo = self.request.GET.get('returnTo', DEFAULT_RETURNTO_PATH)
        self.success_url = returnTo

        initial_data = self.initial.copy() #Copy data loaded automatically to start with
        initial_data.update(model_to_dict(self.request.user)) # Add current user data
        initial_data.update({'returnTo': returnTo})

        return initial_data

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, _('Your profile has been updated.'))
        self.success_url = form.cleaned_data.get('returnTo')
        return super(SocialProfileEditView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.INFO, _('Your profile has NOT been updated.'))
        return super(SocialProfileEditView, self).form_invalid(form)


class DeleteSocialProfileView(DeleteView):
    """
    Account Delete Confirm Modal View

    url: /delete
    """

    success_url = reverse_lazy('sp_logout_page')

    template_name = "socialprofile/sp_delete_account_modal.html"

    model = User

    def get_object(self, queryset=None):
        """Get the object that we are going to delete"""
        return self.request.user
