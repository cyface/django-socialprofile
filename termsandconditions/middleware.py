import urlparse
from django.http import HttpResponseRedirect, QueryDict
from models import TermsAndConditions
from django.conf import settings

if hasattr(settings, 'ACCEPT_TERMS_PATH'):
    ACCEPT_TERMS_PATH = settings.ACCEPT_TERMS_PATH
else:
    ACCEPT_TERMS_PATH = '/terms/accept/'

if hasattr(settings, 'TERMS_RETURNTO_PARAM'):
    TERMS_RETURNTO_PARAM = settings.TERMS_RETURNTO_PARAM
else:
    TERMS_RETURNTO_PARAM = 'returnTo'

if hasattr(settings, 'TERMS_EXCLUDE_URL_PREFIX_LIST'):
    TERMS_EXCLUDE_URL_PREFIX_LIST = settings.TERMS_EXCLUDE_URL_PREFIX_LIST
else:
    TERMS_EXCLUDE_URL_PREFIX_LIST = {'/admin/',}

if hasattr(settings, 'TERMS_EXCLUDE_URL_LIST'):
    TERMS_EXCLUDE_URL_LIST = settings.TERMS_EXCLUDE_URL_LIST
else:
    TERMS_EXCLUDE_URL_LIST = {'/', '/terms/required/',}

class TermsAndConditionslRedirectMiddleware:
    """
    This middleware checks to see if the user is logged in, and if so, if they have accepted the site terms.
    """
    def process_request(self, request):
        if request.user.is_authenticated():
            if not TermsAndConditions.agreed_to_latest(request.user):

                currentPath = request.META['PATH_INFO']
                excludePathFlag = False
                for excludePath in TERMS_EXCLUDE_URL_PREFIX_LIST:
                    if currentPath.startswith(excludePath):
                        excludePathFlag = True

                if currentPath in TERMS_EXCLUDE_URL_LIST:
                    excludePathFlag = True

                if currentPath != ACCEPT_TERMS_PATH and not excludePathFlag:
                    login_url_parts = list(urlparse.urlparse(ACCEPT_TERMS_PATH))
                    querystring = QueryDict(login_url_parts[4], mutable=True)
                    querystring[TERMS_RETURNTO_PARAM] = currentPath
                    login_url_parts[4] = querystring.urlencode(safe='/')
                    return HttpResponseRedirect(urlparse.urlunparse(login_url_parts))