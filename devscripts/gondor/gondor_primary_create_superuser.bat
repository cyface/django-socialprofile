REM This needs to be run from the directory where the .gondor directory lives (socialprofile)
call ..\django-socialprofile-env\Scripts\activate.bat
REM Creates Superuser in primary Gondor Instance
gondor run primary createsuperuser