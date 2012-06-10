"""This file contains functions used as part of a user creation pipeline, such as the one provided by django-social-auth."""
import urlparse
from models import TermsAndConditions
from django.http import HttpResponseRedirect, QueryDict
from django.conf import settings
import logging

ACCEPT_TERMS_PATH = getattr(settings, 'ACCEPT_TERMS_PATH', '/terms/accept/')
TERMS_RETURNTO_PARAM = getattr(settings, 'TERMS_RETURNTO_PARAM', 'returnTo')

LOGGER = logging.getLogger(name='termsandconditions')

def user_accept_terms(backend, user, uid, social_user=None, *args, **kwargs):
    """Show the user the terms and conditions accept page."""

    LOGGER.debug('user_accept_terms')

    if not TermsAndConditions.agreed_to_latest(user):
        return redirect_to_terms_accept('/complete/{0}/'.format(backend.name))
    else:
        return {'social_user': social_user, 'user': user}


def redirect_to_terms_accept(currentPath='/', slug='default'):
    redirect_url_parts = list(urlparse.urlparse(ACCEPT_TERMS_PATH))
    querystring = QueryDict(redirect_url_parts[4], mutable=True)
    querystring[TERMS_RETURNTO_PARAM] = currentPath
    redirect_url_parts[4] = querystring.urlencode(safe='/')
    return HttpResponseRedirect(urlparse.urlunparse(redirect_url_parts))