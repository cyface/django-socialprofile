"""Django Views for the socialprofile module"""

# pylint: disable=R0901,R0904

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.views.generic import DeleteView, TemplateView
from django.utils.translation import ugettext_lazy as _
from .forms import SocialProfileForm, UserForm

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

        next_url = self.request.GET.get(REDIRECT_FIELD_NAME, DEFAULT_RETURNTO_PATH)

        context = super(SelectAuthView, self).get_context_data(**kwargs)
        context['next_param'] = REDIRECT_FIELD_NAME
        context['next_url'] = next_url
        return context


class SocialProfileView(TemplateView):
    """
    Profile View Page

    url: /profile/view
    """
    template_name = 'socialprofile/sp_profile_view.html'

    http_method_names = {'get'}

    def get_context_data(self, **kwargs):
        """Load up the default data to show in the display form."""
        LOGGER.debug("socialprofile.views.SocialProfileView.get_context_data")
        username = self.kwargs.get('username')
        if username:
            user = get_object_or_404(User, username=username)
        elif self.request.user.is_authenticated():
            user = self.request.user
        else:
            raise Http404  # Case where user gets to this view anonymously for non-existent user

        return_to = self.request.GET.get('returnTo', DEFAULT_RETURNTO_PATH)

        sp_form = SocialProfileForm(instance=user.social_profile)
        user_form = UserForm(instance=user)

        sp_form.initial['returnTo'] = return_to

        return {'sp_form': sp_form, 'user_form': user_form}


class SocialProfileEditView(SocialProfileView):
    """
    Profile Editing View

    url: /profile/edit
    """

    template_name = 'socialprofile/sp_profile_edit.html'

    http_method_names = {'get', 'post'}

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST, instance=request.user)
        sp_form = SocialProfileForm(request.POST, instance=request.user.social_profile)

        if user_form.is_valid() & sp_form.is_valid():
            user_form.save()
            sp_form.save()
            messages.add_message(self.request, messages.INFO, _('Your profile has been updated.'))
            return HttpResponseRedirect(sp_form.cleaned_data.get('returnTo', DEFAULT_RETURNTO_PATH))
        else:
            messages.add_message(self.request, messages.INFO, _('Your profile has NOT been updated.'))
            return self.render_to_response({'sp_form': sp_form, 'user_form': user_form})


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
