"""Django Views for the socialprofile-demo module"""
from django.shortcuts import render_to_response
from django.views.decorators.vary import vary_on_cookie
from django.views.decorators.cache import cache_control
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(name='socialprofile')

@vary_on_cookie
def index(request):
    """
    Main site page page.

    url: /
    
    template : socialprofile_demo/index.html
    """

    logger.debug('demo_indexpage')

    response_data = {}

    return render_to_response('socialprofile_demo/index.html', response_data, context_instance=RequestContext(request))

@login_required
@cache_control(must_revalidate=True, max_age=3600)
def secure_view(request):
    """
    Secure testing page.

    url: /secure

    template : socialprofile_demo/secure.html
    """

    logger.debug('securepage')

    response_data = {}

    return render_to_response('socialprofile_demo/secure.html', response_data, context_instance=RequestContext(request))

@login_required
@cache_control(must_revalidate=True, max_age=3600)
def secure_view_too(request):
    """
    Secure testing page.

    url: /securetoo

    template : socialprofile_demo/securetoo.html
    """

    logger.debug('securepagetoo')

    response_data = {}

    return render_to_response('socialprofile_demo/securetoo.html', response_data, context_instance=RequestContext(request))