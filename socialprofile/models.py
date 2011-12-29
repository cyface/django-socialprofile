from social_auth.signals import pre_update
from django.db.models.signals import post_save
from social_auth.backends.facebook import FacebookBackend
from social_auth.backends.google import GoogleOAuth2Backend
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=10)

def facebook_extra_values(sender, user, response, details, **kwargs):
    user.gender = response.get('gender')
    return True

def google_extra_values(sender, user, response, details, **kwargs):
    user.gender = response.get('gender')
    print ("HELLLLLLLOOOOOOOO")
    return True

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

pre_update.connect(facebook_extra_values, sender=FacebookBackend)

pre_update.connect(google_extra_values, sender=GoogleOAuth2Backend)