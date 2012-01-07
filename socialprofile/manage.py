#!/usr/bin/env python
"""Manage.py runs Django Commands with the settings.py in the same dir"""
from django.core.management import execute_manager
#try: # Try/except removed to make sure we see the errors when deploying to Gondor
import settings # Assumed to be in the same directory.
#except ImportError:
#    import sys
#    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
#    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
