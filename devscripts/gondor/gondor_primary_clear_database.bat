REM This needs to be run from the directory where the .gondor directory lives (socialprofile)
call ..\socialprofile-env\Scripts\activate.bat
REM CLEARS DATABASE - AS IN DELETE ALL from primary Gondor Instance
gondor manage primary database:clear