from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import UserProfile

class UserProfileInline(admin.TabularInline):
    model = UserProfile
    fk_name = 'user'
    max_num = 1
    
class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline,]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)