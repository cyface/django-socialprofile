"""Django Views for the termsandconditions module"""
from django.shortcuts import render_to_response
from django.db import IntegrityError
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from forms import TermsAndConditionsForm
from models import TermsAndConditions
from django.conf import settings
from django.http import Http404
import logging

logger = logging.getLogger(name='termsandconditions')

def terms_view (request, slug='default', version_number='latest'):
    """
    View Terms and Conditions Text

    url: /
    
    template : templates/view_terms.html
    """

    logger.debug('index_view')

    try:
        form = TermsAndConditionsForm(slug=slug)
    except TermsAndConditions.DoesNotExist:
        raise Http404

    response_data = {'form': form}

    return render_to_response('termsandconditions/view_terms.html', response_data, context_instance=RequestContext(request))


@login_required
def accept_view(request):
    """
    Terms and Conditions Acceptance view

    url: /terms/accept

    template : templates/accept_terms.html
    """

    logger.debug('accept_view')

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

    response_data = {'form': form}

    return render_to_response('termsandconditions/accept_terms.html', response_data, context_instance=RequestContext(request))