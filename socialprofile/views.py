"""Django Views for the socialprofile module"""
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.db import IntegrityError
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponseRedirect
from forms import SocialProfileForm
from django.views.generic import TemplateView
import logging

LOGGER = logging.getLogger(name='socialprofile')

DEFAULT_RETURNTO_PATH = getattr(settings, 'DEFAULT_RETURNTO_PATH', '/')

def select_view(request):
    """
    Lets users choose how they want to request access.

    url: /select
    
    template : socialprofile/sp_account_select.html
    """

    LOGGER.debug('selectpage')

    nextPage = request.GET.get('next', DEFAULT_RETURNTO_PATH)

    response_data = {'next': nextPage}

    return render_to_response('socialprofile/sp_account_select.html', response_data, context_instance=RequestContext(request))


def profile_view(request, username=None):
    """
    Profile View Page

    url: /

    template : socialprofile/sp_profile_view.html
    """

    LOGGER.debug('profileviewpage')

    if username:
        LOGGER.debug("non-default user:{0}".format(username))
        user = get_object_or_404(User, username=username)
    else:
        user = request.user

    returnTo = request.GET.get('returnTo', DEFAULT_RETURNTO_PATH)

    form = SocialProfileForm(user=user, returnTo=returnTo) # Pass in User to Pre-Populate with Current Values

    response_data = {'form': form}

    return render_to_response('socialprofile/sp_profile_view.html', response_data, context_instance=RequestContext(request))


@login_required
def profile_edit(request):
    """
    Profile Editing Page

    url: /

    template : socialprofile/sp_profile_edit.html
    """

    LOGGER.debug('profileeditpage')

    if request.method == 'POST': # If the form has been submitted...
        form = SocialProfileForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            user = request.user
            form.clean()
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            profile = user.social_profile
            profile.gender = form.cleaned_data['gender']
            profile.url = form.cleaned_data['url']
            profile.image_url = form.cleaned_data['image_url']
            profile.description = form.cleaned_data['description']
            try:
                user.save()
                profile.save()
            except IntegrityError:
                form = SocialProfileForm()
                form._errors = {'username': [u'Your chosen username was not unique.'], }

            messages.add_message(request, messages.INFO, 'Your profile has been updated.')

            returnTo = form.cleaned_data.get('returnTo', DEFAULT_RETURNTO_PATH)
            return HttpResponseRedirect(reverse('sp_profile_view_page') + '?returnTo=' + returnTo)

    else:
        returnTo = request.GET.get('returnTo', DEFAULT_RETURNTO_PATH)
        form = SocialProfileForm(user=request.user, returnTo=returnTo) # Pass in User to Pre-Populate with Current Values

    response_data = {'form': form}

    return render_to_response('socialprofile/sp_profile_edit.html', response_data, context_instance=RequestContext(request))


class DeleteConfirmView(TemplateView):
    """
    Account Delete Confirm Modal View

    url: /delete

    template : socialprofile/sp_delete_account_modal.html
    """

    LOGGER.debug('deleteconfirmpage')

    template_name = "socialprofile/sp_delete_account_modal.html"


@login_required
def delete_action_view(request):
    """
    Account Delete Action view

    url: /delete/action

    template : socialprofile/sp_delete_success.html
    """

    LOGGER.debug('deleteactionpage')

    if request.GET.has_key('confirm'):
        user_to_delete = request.user
        user_to_delete.delete()
        logout(request)

        response_data = {}

        return render_to_response('socialprofile/sp_delete_success.html', response_data, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse('sp_delete_confirm_view'))
