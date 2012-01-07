"""Django Admin Site configuration for socialprofiles"""

# pylint: disable=R0904

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import UserProfile

class UserProfileInline(admin.TabularInline):
    """Sets up UserProfile to be inline editable along with users"""
    model = UserProfile
    fk_name = 'user'
    max_num = 1
    
class CustomUserAdmin(UserAdmin):
    """Sets up the custom user admin display"""
    inlines = [UserProfileInline,]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)