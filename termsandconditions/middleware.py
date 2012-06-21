import urlparse
from django.http import HttpResponseRedirect, QueryDict
from models import TermsAndConditions
from django.conf import settings
from pipeline import redirect_to_terms_accept

ACCEPT_TERMS_PATH = getattr(settings, 'ACCEPT_TERMS_PATH', '/terms/accept/')
TERMS_EXCLUDE_URL_PREFIX_LIST = getattr(settings, 'TERMS_EXCLUDE_URL_PREFIX_LIST', {'/admin/',})
TERMS_EXCLUDE_URL_LIST = getattr(settings, 'TERMS_EXCLUDE_URL_LIST', {'/', '/terms/required/', '/socialprofile/logout/', '/securetoo/'})

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
                    return redirect_to_terms_accept(currentPath)