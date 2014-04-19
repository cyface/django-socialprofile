#!/bin/bash
. .env/bin/activate
python manage.py jenkins --coverage-rcfile=devscripts/checkers/coveragerc socialprofile
python manage.py pylint --pylint-file-output --pylint-rcfile=devscripts/checkers/pylintrc socialprofile socialprofile_demo