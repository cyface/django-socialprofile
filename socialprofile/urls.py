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
    
    # Select Sign Up Method
    url(r'^select/$', 'socialprofile.views.select_view', name="select_page"),

    # Profile
    url(r'^profile/$', 'socialprofile.views.profile_view', name="profile_page"),

    # Social Registration
    url(r'', include('social_auth.urls')),
    
    # Logout Page
    url(r'^logout/$', 'socialprofile.views.logout_view', name="logout_page"),
      
)