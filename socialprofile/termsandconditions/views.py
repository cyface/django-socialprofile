"""Django Views for the termsandconditions module"""
from django.shortcuts import render_to_response
from django.db import IntegrityError
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from forms import TermsAndConditionsForm
from models import TermsAndConditions
from django.conf import settings
from django.http import Http404
from django.views.generic import TemplateView
import logging

logger = logging.getLogger(name='termsandconditions')

class TermsView (TemplateView):
    template_name = 'termsandconditions/view_terms.html'

    logger.debug('TemplateView')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TermsView, self).get_context_data(**kwargs)
        try:
            slug = 'site-terms'
            form = TermsAndConditionsForm(slug=slug)
            context['form'] = form
        except TermsAndConditions.DoesNotExist:
            raise Http404

        return context

    def get_urls(self):
        from django.conf.urls.defaults import patterns, url

        urlpatterns = patterns('',
            url(r'^terms/', TermsView.as_view(), name='terms_terms_view'),
        )
        return urlpatterns
    urls = property(get_urls)


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