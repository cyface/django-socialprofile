"""
    Master URL Pattern List for the application.  Most of the patterns here should be top-level
    pass-offs to sub-modules, who will have their own urls.py defining actions within.
"""

# pylint: disable=E1120

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from views import IndexView, SecureView
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView, TemplateView

admin.autodiscover()

urlpatterns = (
    # Home Page
    url(r'^$', never_cache(IndexView.as_view()), name="sp_demo_home_page"),

    # Secure Page
    url(r'^secure/$', never_cache((login_required(SecureView.as_view()))),
        name="sp_demo_secure_page"),

    # Secure Page Too
    url(r'^securetoo/$',
        never_cache(login_required(SecureView.as_view(template_name="securetoo.html"))),
        name="sp_demo_secure_page_too"),

    # Social Profile & Social Auth
    url(r'^socialprofile/', include('socialprofile.urls')),

    # Admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin Site:
    url(r'^admin/', include(admin.site.urls)),

    # Robots and Favicon
    url(r'^robots\.txt$', TemplateView.as_view(),
        {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    url(r'^favicon\.ico$', RedirectView.as_view(), {'url': settings.STATIC_URL + 'images/favicon.ico'}),
)
