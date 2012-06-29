#!/bin/sh
#Deploys current checked-in master branch to primary Gondor Instance
#This needs to be run from the directory where the gondor.yml file lives
. ./django-socialprofile-env/bin/activate
gondor deploy primary master