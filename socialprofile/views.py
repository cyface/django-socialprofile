from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


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

def select_view(request):
    """
    Lets users choose how they want to request access.

    url: /select
    
    template : templates/select.html
    """                      
    
    response_data = {}
    
    return render_to_response('select.html', response_data, context_instance=RequestContext(request))

@login_required
def secure_view(request):
    """
    Secure testing page.

    url: /secure
    
    template : templates/secure.html
    """                      
    
    response_data = {}
    
    return render_to_response('secure.html', response_data, context_instance=RequestContext(request))
    