"""Django Views for the termsandconditions module"""
from django.shortcuts import render_to_response
from django.db import IntegrityError
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from forms import TermsAndConditionsForm
from models import TermsAndConditions, UserTermsAndConditions
from decorators import terms_required
from django.http import Http404, HttpResponseRedirect
from django.views.generic import TemplateView
import datetime
import logging

logger = logging.getLogger(name='termsandconditions')

class ViewTerms(TemplateView):
    template_name = 'termsandconditions/view_terms.html'

    logger.debug('termsviewpage')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ViewTerms, self).get_context_data(**kwargs)
        try:
            slug = 'site-terms'
            form = TermsAndConditionsForm(slug=slug)
            context['form'] = form
        except TermsAndConditions.DoesNotExist:
            raise Http404

        return context

    def get_urls(self):
        from django.conf.urls import patterns, url

        urlpatterns = patterns('',
            url(r'^$', ViewTerms.as_view(), name='terms_index'),
            url(r'^view/$', ViewTerms.as_view(), name='terms_view'),
        )
        return urlpatterns

    urls = property(get_urls)


def accept_view(request):
    """
    Terms and Conditions Acceptance view

    url: /terms/accept

    template : templates/accept_terms.html
    """

    logger.debug('termsacceptpage')

    if request.method == 'POST': # If the form has been submitted...
        if request.user.is_authenticated():
            user = request.user
        else:
            if request.session.has_key('partial_pipeline'):
                user_pk = request.session['partial_pipeline']['kwargs']['user']['pk']
                user = User.objects.get(id=user_pk)
            else:
                return HttpResponseRedirect('/')

        form = TermsAndConditionsForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            #user = request.user
            form.clean()
            try:
                terms = TermsAndConditions.objects.get(slug=form.cleaned_data['slug'], version_number=form.cleaned_data['version_number'])
                userTerms = UserTermsAndConditions()
                userTerms.terms=terms
                userTerms.user=user
                userTerms.date_accepted=datetime.datetime.now()
                userTerms.ip_address=request.META['REMOTE_ADDR']
                userTerms.save()
                if form.cleaned_data.has_key('returnTo'):
                    return HttpResponseRedirect(form.cleaned_data['returnTo'])
            except IntegrityError as err:
                logger.error('Integrity Error Saving Terms and Conditions', err)
    else:
        form = TermsAndConditionsForm() # Pass in User to Pre-Populate with Current Values
        if request.GET.has_key('returnTo') :
            form.initial['returnTo'] = request.GET['returnTo']

    response_data = {'form': form, }


    return render_to_response('termsandconditions/accept_terms.html', response_data,
        context_instance=RequestContext(request))

@login_required
@terms_required
def terms_required_view(request):
    """
    Terms Required testing page.

    url: /terms_required

    template : templates/terms_required.html
    """

    logger.debug('termsrequiredpage')

    response_data = {}

    return render_to_response('termsandconditions/terms_required.html', response_data, context_instance=RequestContext(request))