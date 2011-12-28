"""
Local Django Settings File

INSTRUCTIONS
SAVE A COPY OF THIS FILE IN THIS DIRECTORY WITH THE NAME settings_local.py
MAKE YOUR LOCAL SETTINGS CHANGES IN THAT FILE AND DO NOT CHECK IT IN
CHANGES TO THIS FILE SHOULD BE TO ADD/REMOVE SETTINGS THAT NEED TO BE
MADE LOCALLY BY ALL INSTALLATIONS

settings_local.py, once created, should never be checked into source control
It is ignored by default by .gitignore, so if you don't mess with that, you should be fine.
"""
# pylint: disable=R0801, W0611
import os
from settings_main import MIDDLEWARE_CLASSES, INSTALLED_APPS

# Set the root path of the project so it's not hard coded
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
# IP Addresses that should be treated as internal/debug users
INTERNAL_IPS = ('127.0.0.1',)

# Cache Settings
# CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_BACKEND = 'dummy:///'
CACHE_MIDDLEWARE_SECONDS = 30
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
CACHE_MIDDLEWARE_KEY_PREFIX = 'sp'

# List of Admin users to be emailed by error system
MANAGERS = (
    # ('Tim White', 'tim@cyface.com'),
)
ADMINS = MANAGERS

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory that holds media.
# Note that as of Django 1.3 - media is for uploaded files only.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")

#Staticfiles Config
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
STATIC_URL = '/static/'
STATICFILES_DIRS = [ os.path.join(PROJECT_ROOT, 'themes') ]

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = os.path.join(STATIC_URL, 'admin')

# Local DB settings. (Postgres)
DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'pb2',
#        'USER': 'pb2',
#        'PASSWORD': '',
#        'HOST': '127.0.0.1',
#        'PORT': '', # Set to empty string for default.
#        'SUPPORTS_TRANSACTIONS': 'true',
#    },
     'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sp',
        'USER': 'sp',
        'PASSWORD': '',
#        'HOST': '127.0.0.1',
#        'PORT': '', # Set to empty string for default.
#        'SUPPORTS_TRANSACTIONS': 'true',
    }
}

# Local DB settings. (MySQL)
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'pb2',
#        'USER': 'pb2',
#        'PASSWORD': '',
#        'HOST': '127.0.0.1',
#        'PORT': '', # Set to empty string for default.
#        'SUPPORTS_TRANSACTIONS': 'false',
#        'OPTIONS': {'init_command': 'SET storage_engine=INNODB'},
#    }
#}

# Local DB settings. (SQLLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_ROOT + '/socialprofile.db',
        'SUPPORTS_TRANSACTIONS': 'false',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Denver'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'zv$+w7juz@(g!^53o0ai1u082)=jkz9my_r=3)fglrj5t8l$2#'

# Email Settings
EMAIL_HOST = 'a real smtp server'
EMAIL_HOST_USER = 'your_mailbox_username'
EMAIL_HOST_PASSWORD = 'your_mailbox_password'
DEFAULT_FROM_EMAIL = 'a real email address'
SERVER_EMAIL = 'a real email address'

### TESTS
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner' # Should work with Django 1.2.1

### Local add-ons to main inclusion variables
# TEMPLATE_CONTEXT_PROCESSORS +=

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
)

##### Custom Variables Below Here #######

# Django SocialRegistration Settings
SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook', 'google-oauth2', 'twitter')

TWITTER_CONSUMER_KEY         = 'gvlRdtanILw15YXxKGIA'
TWITTER_CONSUMER_SECRET      = 'acw6IiDtt5kJrmUI8WJVHAENmnCSllpqlM13dQPI'
FACEBOOK_APP_ID              = '295912813778057'
FACEBOOK_API_SECRET          = 'bb0c4233c822875650962953aad4c40e'
GOOGLE_OAUTH2_CLIENT_ID      = '349612856343.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = 'xUP-iEWhZBc7NqDEuWt5Nvu0'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/'
#SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account-disconnected-redirect-url/'
#SOCIAL_AUTH_ERROR_KEY = 'social_errors' # In case of authentication error, the message can be stored in session if this setting is defined
#SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
#SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'
#SOCIAL_AUTH_USERNAME_FIXER = lambda u: slugify(u)
#SOCIAL_AUTH_UUID_LENGTH = 16
#SOCIAL_AUTH_EXTRA_DATA = False
#SOCIAL_AUTH_EXPIRATION = 'expires'
#SOCIAL_AUTH_SESSION_EXPIRATION = False
#SOCIAL_AUTH_USER_MODEL = 'myapp.CustomUser'
#SOCIAL_AUTH_CREATE_USERS = False
#FACEBOOK_AUTH_EXTRA_ARGUMENTS = {'display': 'touch'}
#SOCIAL_AUTH_INACTIVE_USER_URL = '...'

SOCIAL_AUTH_ASSOCIATE_BY_MAIL = True # Groups accounts by email address
SOCIAL_AUTH_DEFAULT_USERNAME = 'Inigo Montoya'

LOGIN_URL          = '/login/google-oauth2'
#LOGIN_REDIRECT_URL = '/logged-in/'
#LOGIN_ERROR_URL    = '/login-error/'

### django-registration Settings
ACCOUNT_ACTIVATION_DAYS = 14

### DEBUG TOOLBAR
if DEBUG:
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )
    
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False
    }

### SECURE SITE
# SSL_SITE_LOGIN_URL = '' # URL to HTTPS version of site for secure sign-in.

### LOGGING
#if DEBUG:
#    import logging
#    logging.basicConfig(level=logging.DEBUG,
#        format='%(asctime)s %(levelname)s %(message)s',
#        filename=os.path.join(PROJECT_ROOT, 'django.log'),
#        filemode='a+')