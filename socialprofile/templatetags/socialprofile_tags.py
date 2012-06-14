"""Template tags for the socialprofile module"""

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def social_provider_name(provider_slug):
    if provider_slug == 'google-oauth2':
        return "Google"

    if provider_slug == 'twitter':
        return "Twitter"

    if provider_slug == 'facebook':
        return "Facebook"
