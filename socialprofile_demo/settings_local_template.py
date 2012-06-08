"""
Local Django Settings File

INSTRUCTIONS
SAVE A COPY OF THIS FILE IN THIS DIRECTORY WITH THE NAME local_settings.py
MAKE YOUR LOCAL SETTINGS CHANGES IN THAT FILE AND DO NOT CHECK IT IN
CHANGES TO THIS FILE SHOULD BE TO ADD/REMOVE SETTINGS THAT NEED TO BE
MADE LOCALLY BY ALL INSTALLATIONS

local_settings.py, once created, should never be checked into source control
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
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'mediaroot')

#Staticfiles Config
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticroot')
STATIC_URL = '/static/'
STATICFILES_DIRS = [ os.path.join(PROJECT_ROOT, 'static')  ]
TEMPLATE_DIRS = [os.path.join(PROJECT_ROOT, 'templates')]

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Local DB settings. (Postgres)
DATABASES = {
    #    'default': {
    #        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #        'NAME': 'socialprofile',
    #        'USER': 'socialprofile',
    #        'PASSWORD': '',
    #        'HOST': '127.0.0.1',
    #        'PORT': '', # Set to empty string for default.
    #        'SUPPORTS_TRANSACTIONS': 'true',
    #    },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_ROOT + '/socialprofile.db',
        'SUPPORTS_TRANSACTIONS': 'false',
        }
}

# Python dotted path to the WSGI application used by Django's runserver.
#WSGI_APPLICATION = 'socialprofile_demo.wsgi.application'

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

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'zv$+w7juz@(g!^53o0ai1u082)=jkz9my_r=3)fglrj5t8l$2#'

# Email Settings
EMAIL_HOST = 'a real smtp server'
EMAIL_HOST_USER = 'your_mailbox_username'
EMAIL_HOST_PASSWORD = 'your_mailbox_password'
DEFAULT_FROM_EMAIL = 'a real email address'
SERVER_EMAIL = 'a real email address'

### TESTS
#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner' # Should work with Django 1.2.1

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
# Below is the main facebook key
FACEBOOK_APP_ID              = '295912813778057'
FACEBOOK_API_SECRET          = 'bb0c4233c822875650962953aad4c40e'
#Below is localhost facebook key
#FACEBOOK_APP_ID              = '316069408433708'
#FACEBOOK_API_SECRET          = '9b1d6707b2d709c6282fa65ec54fb0af'
FACEBOOK_EXTENDED_PERMISSIONS = ['email',]
GOOGLE_OAUTH2_CLIENT_ID      = '349612856343.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = 'xUP-iEWhZBc7NqDEuWt5Nvu0'
GOOGLE_OAUTH_EXTRA_SCOPE     = ['https://www.googleapis.com/auth/userinfo.profile',] # Note that this extra scope is not the same as the API URL we use

SOCIAL_AUTH_CHANGE_SIGNAL_ONLY = True # Prevent updating of name, etc. once user is created
SOCIAL_AUTH_ASSOCIATE_BY_MAIL = True # Try and connect accounts with the same email address

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/profile'
#SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/accept'
#SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/'

LOGIN_URL          = '/select'
#LOGIN_REDIRECT_URL = '/logged-in/'
#LOGIN_ERROR_URL    = '/'

### django-registration Settings
ACCOUNT_ACTIVATION_DAYS = 14

### TermsAndConditions
DEFAULT_TERMS_SLUG = 'site-terms'

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

#### LOGGING
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,''
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        }
}