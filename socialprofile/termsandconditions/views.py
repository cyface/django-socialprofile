"""Django Views for the termsandconditions module"""
from django.shortcuts import render_to_response
from django.db import IntegrityError
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from forms import TermsAndConditionsForm
import logging

logger = logging.getLogger(name='termsandconditions')

def index(request):
    """
    Main site page page.

    url: /
    
    template : templates/index.html
    """

    logger.debug('indexpage')

    response_data = {}

    return render_to_response('index.html', response_data, context_instance=RequestContext(request))


@login_required
def accept_view(request):
    """
    Terms and Conditions Acceptance view

    url: /acceptterms

    template : templates/accept_terms.html
    """

    if request.method == 'POST': # If the form has been submitted...
        form = TermsAndConditionsForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            user = request.user
            form.clean()
            try:
                pass
            except IntegrityError:
                pass


    else:
        form = TermsAndConditionsForm() # Pass in User to Pre-Populate with Current Values

    response_data = {'form': form, 'errors': form.errors}

    return render_to_response('templates/accept_terms.html', response_data, context_instance=RequestContext(request))