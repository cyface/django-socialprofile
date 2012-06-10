"""Django Views for the socialprofile-demo module"""
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(name='socialprofile')

def index(request):
    """
    Main site page page.

    url: /
    
    template : templates/index.html
    """

    logger.debug('demo_indexpage')

    response_data = {}

    return render_to_response('index.html', response_data, context_instance=RequestContext(request))

@login_required
def secure_view(request):
    """
    Secure testing page.

    url: /secure

    template : templates/secure.html
    """

    logger.debug('securepage')

    response_data = {}

    return render_to_response('secure.html', response_data, context_instance=RequestContext(request))

@login_required
def secure_view_too(request):
    """
    Secure testing page.

    url: /securetoo

    template : templates/securetoo.html
    """

    logger.debug('securepagetoo')

    response_data = {}

    return render_to_response('securetoo.html', response_data, context_instance=RequestContext(request))