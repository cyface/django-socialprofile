"""Template tags for the socialprofile module"""

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.translation import ugettext as _

register = template.Library()


@register.filter
@stringfilter
def social_provider_name(provider_slug):
    """Decode name of Social Auth Provider to Friendly Name"""
    if provider_slug == 'google-oauth2':
        return _("Google")

    if provider_slug == 'twitter':
        return _("Twitter")

    if provider_slug == 'facebook':
        return _("Facebook")
