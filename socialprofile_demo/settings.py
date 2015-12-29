"""
Django Settings File
"""
# pylint: disable=R0801, W0611

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEMO_DIR = os.path.join(BASE_DIR, 'socialprofile_demo')

# Explicitly Define test runner to silence 1_6.W001 Warning
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

DEBUG = True
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
    # ('Your Name', 'you@you.com'),
)
ADMINS = MANAGERS

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory that holds media.
MEDIA_ROOT = os.path.join(DEMO_DIR, 'mediaroot')

# Staticfiles Config
STATIC_ROOT = os.path.join(DEMO_DIR, 'staticroot')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(DEMO_DIR, 'static')]

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Local DB settings. (Postgres)
DATABASES = {
    # 'default': {
    # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
    # 'NAME': 'socialprofile',
    # 'USER': 'socialprofile',
    # 'PASSWORD': '',
    # 'HOST': '127.0.0.1',
    #        'PORT': '', # Set to empty string for default.
    #        'SUPPORTS_TRANSACTIONS': 'true',
    #    },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DEMO_DIR, 'socialprofile.db'),
        'SUPPORTS_TRANSACTIONS': 'false',
    }
}

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'socialprofile_demo.wsgi.application'

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
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'zv$+w7juz@(g!^53o0ai1u082)=jkz9mT_r=3)fglrj5t8l$2#'

# Email Settings
EMAIL_HOST = 'a real smtp server'
EMAIL_HOST_USER = 'your_mailbox_username'
EMAIL_HOST_PASSWORD = 'your_mailbox_password'
DEFAULT_FROM_EMAIL = 'a real email address'
SERVER_EMAIL = 'a real email address'

""" Django settings for the project. """

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(DEMO_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
            'debug': DEBUG,
        },
    },
]

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'socialprofile_demo.urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django_jenkins',
    'socialprofile',
    'socialprofile_demo',
    'social.apps.django_app.default',
)

# #### Custom Variables Below Here #######

# Python Socialauth Settings

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Leave Enabled for Admin Access
    'social.backends.twitter.TwitterOAuth',
    'social.backends.facebook.Facebook2OAuth2',
    'social.backends.google.GoogleOAuth2',
)

SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.debug.debug',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'socialprofile.pipeline.socialprofile_extra_values',
    'social.pipeline.debug.debug'
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/secure/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/secure/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/secure/'

# Core Authentication Settings
LOGIN_URL = '/socialprofile/select/'
LOGIN_REDIRECT_URL = '/secure/'
LOGIN_ERROR_URL = '/socialprofile/select/'

# Logging
LOGGING = {
    'version': 1,
    "disable_existing_loggers": False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        "root": {
            "handlers": ["console"],
            'propagate': True,
            "level": "INFO",
        },
        'socialprofile': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

try:
    from socialprofile_demo.local_settings import *
except ImportError:
    pass