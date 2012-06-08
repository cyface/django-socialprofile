import urlparse
from django.http import HttpResponseRedirect, QueryDict
from models import TermsAndConditions
#from django.conf import settings

ACCEPT_TERMS_PATH = '/terms/accept/'

class TermsAndConditionslRedirectMiddleware:
    """
    This middleware checks to see if the user is logged in, and if so, if they have accepted the site terms.
    """
    def process_request(self, request):
        if request.user.is_authenticated():
            if not TermsAndConditions.agreed_to_latest(request.user):
                currentPath = request.META['PATH_INFO']
                if currentPath != ACCEPT_TERMS_PATH and not currentPath.startswith('/admin'):
                    login_url_parts = list(urlparse.urlparse(ACCEPT_TERMS_PATH))
                    querystring = QueryDict(login_url_parts[4], mutable=True)
                    querystring['returnTo'] = currentPath
                    login_url_parts[4] = querystring.urlencode(safe='/')
                    return HttpResponseRedirect(urlparse.urlunparse(login_url_parts))