#!/bin/sh
#Deploys current checked-in master branch to primary Gondor Instance
. ./django-socialprofile-env/bin/activate
gondor deploy primary master