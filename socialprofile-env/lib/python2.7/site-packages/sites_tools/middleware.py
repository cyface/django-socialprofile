from django.conf import settings
from django.utils.cache import patch_vary_headers

from django.contrib.sites.models import Site, RequestSite, SITE_CACHE

class CaseInsensitiveRequestSite(RequestSite):
    """
    A subclass of django.contrib.sites.models.RequestSite
    which uses a case insensitive host name.
    """
    def __init__(self, request):
        self.domain = self.name = request.get_host().lower()

class LazySite(object):
    """
    A lazy site object that refers to either Site instance or
    a case insensitive RequestSite.
    """
    def get_site(self, request):
        host = request.get_host().lower()
        if ':' in host:
            host, _ = host.split(':', 1)
        # First check, if there are any cached sites
        site = SITE_CACHE.get(host, None)
        if site is None:
            if Site._meta.installed:
                # Secondly, find the matching Site objects and set the cache
                matches = Site.objects.filter(domain__iexact=host)
                try:
                    site = matches[0]
                except IndexError:
                    site = None
            else:
                site = CaseInsensitiveRequestSite(request)
            SITE_CACHE[host] = site
        return site

    def __get__(self, request, obj_type=None):
        if not hasattr(request, '_cached_site'):
            request._cached_site = self.get_site(request)
        return request._cached_site


class SitesMiddleware(object):

    def process_request(self, request):
        if not hasattr(request.__class__, 'site'):
            request.__class__.site = LazySite()
        return None

    def process_response(self, request, response):
        """
        Forces the HTTP Vary header onto requests to avoid having responses
        cached from incorrect urlconfs.

        If you'd like to disable this for some reason, set `FORCE_VARY_ON_HOST`
        in your Django settings file to `False`.
        """
        if getattr(settings, 'SITES_VARY_ON_HOST', True):
            patch_vary_headers(response, ('Host',))
        return response

