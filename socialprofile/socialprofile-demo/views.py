"""Django Views for the socialprofile-demo module"""
from django.shortcuts import render_to_response
from django.db import IntegrityError
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from forms import ProfileForm
import logging

logger = logging.getLogger(name='socialprofile')

def index(request):
    """
    Main site page page.

    url: /
    
    template : templates/index.html
    """

    logger.debug('indexpage')

    response_data = {}

    return render_to_response('index.html', response_data, context_instance=RequestContext(request))