REM This script does everything needed to get the package in PyPi - it should be run from the same dir that setup.py is in

python setup.py register sdist bdist_dumb bdist_wininst upload