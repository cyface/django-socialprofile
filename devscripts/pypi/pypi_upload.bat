REM This script updates the distributions and uploads them to PuPi - it should be run from the same dir that setup.py is in

python setup.py sdist bdist_dumb bdist_wininst upload