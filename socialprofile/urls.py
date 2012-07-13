"""
    Master URL Pattern List for the application.  Most of the patterns here should be top-level
    pass-offs to sub-modules, who will have their own urls.py defining actions within.
"""

# pylint: disable=W0401, W0614, E1120

from django.conf.urls import *  #@UnusedWildImport
from django.contrib import admin
from socialprofile.views import SelectAuthView, SocialProfileView, SocialProfileEditView, DeleteSocialProfileView
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

admin.autodiscover()

urlpatterns = patterns('',

    # Profile Self View
    url(r'^$', never_cache(SocialProfileView.as_view()), name="sp_profile_view_page"),

    # Profile Other View
    url(r'^view/(?P<username>\w+)/$', SocialProfileView.as_view(), name="sp_profile_other_view_page"),

    # Profile Edit
    url(r'^edit/$', never_cache(login_required(SocialProfileEditView.as_view())), name="sp_profile_edit_page"),

    # Select Sign Up Method
    url(r'^select/$', never_cache(SelectAuthView.as_view()), name="sp_select_page"),

    # Delete
    url(r'^delete/$', login_required(DeleteSocialProfileView.as_view()), name="sp_delete_page"),

    # Social Auth
    url(r'^socialauth/', include('social_auth.urls')),

    # Logout Page
    url(r'^logout/$', 'django.contrib.auth.views.logout', kwargs={'next_page': "/"}, name="sp_logout_page"),

)