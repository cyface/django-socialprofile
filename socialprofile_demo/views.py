"""Django Views for the socialprofile-demo module"""
from django.shortcuts import render_to_response
from django.views.decorators.cache import never_cache
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(name='socialprofile')

@never_cache
def index(request):
    """
    Main site page page.

    url: /
    
    template : socialprofile_demo/index.html
    """

    logger.debug('socialprofile_demo.views.index')

    response_data = {}

    return render_to_response('socialprofile_demo/index.html', response_data, context_instance=RequestContext(request))

@login_required
@never_cache
def secure_view(request):
    """
    Secure testing page.

    url: /secure

    template : socialprofile_demo/secure.html
    """

    logger.debug('socialprofile_demo.views.secure_view')

    response_data = {}

    return render_to_response('socialprofile_demo/secure.html', response_data, context_instance=RequestContext(request))

@login_required
@never_cache
def secure_view_too(request):
    """
    Secure testing page.

    url: /securetoo

    template : socialprofile_demo/securetoo.html
    """

    logger.debug('socialprofile_demo.views.secure_view_too')

    response_data = {}

    return render_to_response('socialprofile_demo/securetoo.html', response_data, context_instance=RequestContext(request))