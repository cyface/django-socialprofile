REM This needs to be run from the directory where the gondor.yml file lives
call django-socialprofile-env\Scripts\activate.bat
REM This deploys the currently checked-in GIT Master Branch to the primary Gondor Instance
gondor deploy primary master