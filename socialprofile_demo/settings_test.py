"""Automated Unit Test Settings File for the Project"""

# pylint: disable=W0401, W0614, E0611, F0401

from settings_main import * #@UnusedWildImport
from settings_local_template import * #@UnusedWildImport

try:
    from socialprofile_demo.settings_test_local import * #@UnusedWildImport
except:
    pass
import tempfile

# Test DB settings. (SQLLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'test_sqlite.db'),
        'TEST_NAME': os.path.join(PROJECT_ROOT, 'test_sqlite.db'),
    }
}

# Test Cache Settings
CACHE_BACKEND = "file://" + tempfile.gettempdir()

INSTALLED_APPS += ('django_nose',)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner' # Should work with Django 1.2.1+