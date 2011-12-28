from django.utils.decorators import decorator_from_middleware

from sites_tools.middleware import SitesMiddleware

site_aware = decorator_from_middleware(SitesMiddleware)
site_aware.__name__ = "site_aware"
site_aware.__doc__ = """
This decorator adds a LazySite instance to the request in exactly the same
way as the SitesMiddleware, but it can be used on a per view basis.
"""
