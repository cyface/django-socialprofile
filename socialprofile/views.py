from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout


def index(request):
    """
    Main site page page.

    url: /
    
    template : templates/index.html
    """                      
    
    response_data = {}
    
    return render_to_response('index.html', response_data, context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    response_data = {}
    return render_to_response('index.html', response_data, context_instance=RequestContext(request))