"""Django settings for the project."""

# pylint: disable=E0611,F0401,W0401,W0614

# NOTE
# see settings_local.template for instructions on making your local settings file

from settings_main import * #@UnusedWildImport

try:
    from settings_local import * #@UnusedWildImport
except ImportError:
    from settings_local_template import * #@UnusedWildImport
    print("ERROR: You need to rename settings_local.template to settings_local.py and customize it.")
    
# Import Gondor auto-generated local settings if they exist.
try:
    from local_settings import *
except ImportError:
    pass