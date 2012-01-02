"""
    Master URL Pattern List for the application.  Most of the patterns here should be top-level
    pass-offs to sub-modules, who will have their own urls.py defining actions within.
"""

from django.conf.urls.defaults import *  #@UnusedWildImport
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Home Page
    url(r'^$', 'socialprofile.views.index', name="home_page"),
    
    # Secure Page
    url(r'^secure$', 'socialprofile.views.secure_view', name="secure_page"),
    
    # Sign Up
    url(r'^select$', 'socialprofile.views.select_view', name="select_page"),

    # Profile
    url(r'^profile', 'socialprofile.views.profile_view', name="profile_page"),
    
    # Social Registration
    url(r'', include('social_auth.urls')),
    
    # Logout Page
    url(r'^logout$', 'socialprofile.views.logout_view', name="logout_page"),
    
    # Admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin Site:
    (r'^admin/', include(admin.site.urls)),
      
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