"""
    Master URL Pattern List for the application.  Most of the patterns here should be top-level
    pass-offs to sub-modules, who will have their own urls.py defining actions within.
"""

# pylint: disable=W0401, W0614

from django.conf.urls import *  #@UnusedWildImport
from django.contrib import admin
from django.contrib.auth.views import logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from socialprofile.views import DeleteConfirmView

admin.autodiscover()

urlpatterns = patterns('',

    # Profile Self View
    url(r'^$', 'socialprofile.views.profile_view', name="sp_profile_view_page"),

    # Profile Other View
    url(r'^view/(?P<username>\w+)/$', 'socialprofile.views.profile_view', name="sp_profile_other_view_page"),

    # Profile Edit
    url(r'^edit/$', 'socialprofile.views.profile_edit', name="sp_profile_edit_page"),

    # Select Sign Up Method
    url(r'^select/$', 'socialprofile.views.select_view', name="sp_select_page"),

    # Delete Confirm Modal
    url(r'^delete/$', DeleteConfirmView.as_view(), name="sp_delete_confirm_page"),

    # Delete
    url(r'^delete/action/$', 'socialprofile.views.delete_action_view', name="sp_delete_action_page"),

    # Social Auth
    url(r'^socialauth/', include('social_auth.urls')),
    
    # Logout Page
    url(r'^logout/$', 'django.contrib.auth.views.logout', kwargs={'next_page':"/"},name="sp_logout_page"),
      
)