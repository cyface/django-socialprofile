"""Django Views for the socialprofile-demo module"""
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """
    Main site page page.

    url: /
    """

    template_name = "index.html"


class SecureView(TemplateView):
    """
    Secure testing page.

    url: /secure & /securetoo
    """

    template_name = "secure.html"