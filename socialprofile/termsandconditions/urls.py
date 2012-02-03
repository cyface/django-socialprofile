"""
    Master URL Pattern List for the application.  Most of the patterns here should be top-level
    pass-offs to sub-modules, who will have their own urls.py defining actions within.
"""

# pylint: disable=W0401, W0614

from django.conf.urls.defaults import *  #@UnusedWildImport
from django.views.generic import RedirectView
from django.contrib import admin
from django.core.urlresolvers import reverse

admin.autodiscover()

urlpatterns = patterns('termsandconditions.views',
    # View Terms
    url(r'^$', 'terms_view'),
    url(r'^view/$', 'terms_view', name="view_terms_page"),
    url(r'^view/(?P<slug>[-\w]+)/$', 'terms_view', name="view_terms_page_with_slug"),

    # Accept Terms
    url(r'^accept/$', 'accept_view', name="terms_accept_page"),
)


#
#url(r'^(?P<slug>\[-w])/(?P<version_number>\[0..9\.]+)$', 'accept_view', name="view_terms_page_with_version"),