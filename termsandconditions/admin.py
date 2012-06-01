"""Django Admin Site configuration for socialprofiles"""

# pylint: disable=R0904

from django.contrib import admin
from models import TermsAndConditions
    
class TermsAndConditionsAdmin(admin.ModelAdmin):
    """Sets up the custom user admin display"""
    list_display = ('slug', 'name', 'date_active', 'version_number',)

admin.site.register(TermsAndConditions, TermsAndConditionsAdmin)