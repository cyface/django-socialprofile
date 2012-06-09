"""Django Views for the socialprofile-demo module"""
from django.shortcuts import render_to_response
from django.template import RequestContext
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