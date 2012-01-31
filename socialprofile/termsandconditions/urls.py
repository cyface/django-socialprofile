"""
    Master URL Pattern List for the application.  Most of the patterns here should be top-level
    pass-offs to sub-modules, who will have their own urls.py defining actions within.
"""

# pylint: disable=W0401, W0614

from django.conf.urls.defaults import *  #@UnusedWildImport
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Home Page
    url(r'^$', 'termsandconditions.views.index', name="home_page"),

    # Accept Terms
    url(r'^profile', 'termsandconditions.views.accept_view', name="profile_page"),
)

#Only hook up the static and media to run through Django in a dev environment...in prod, needs to be handled by web server
# Staticfiles Setup
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )