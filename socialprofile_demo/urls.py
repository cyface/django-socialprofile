"""
    Master URL Pattern List for the application.  Most of the patterns here should be top-level
    pass-offs to sub-modules, who will have their own urls.py defining actions within.
"""

# pylint: disable=W0401, W0614
from django.conf.urls import *  #@UnusedWildImport
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

    # Home Page
    url(r'^$', 'socialprofile.views.index', name="home_page"),

    # Secure Page
    url(r'^secure/$', 'socialprofile_demo.views.secure_view', name="secure_page"),

    # Secure Page Too
    url(r'^securetoo/$', 'socialprofile_demo.views.secure_view_too', name="secure_page_too"),

    # Social Profiles
    url(r'', include('socialprofile.urls')),

    # Terms and Conditions
    url(r'^terms/', include('termsandconditions.urls')),

    # Social Registration
    url(r'', include('social_auth.urls')),
    
    # Admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin Site:
    (r'^admin/', include(admin.site.urls)),
      
)

#Only hook up the static and media to run through Django in a dev environment...in prod, needs to be handled by web server
# Staticfiles Setup
#if settings.DEBUG:
#    urlpatterns += staticfiles_urlpatterns()
#    urlpatterns += patterns('',
#        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#            'document_root': settings.MEDIA_ROOT,
#        }),
#   )