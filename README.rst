Django Social Profile
=====================

Django Social Profile gives you an out-of-the-box way to let users create an account in your application using
Google, Twitter, or Facebook authentication.

Users can edit their profile, view other users' profiles, and add multiple types of auth to the same profile.

A `Terms and Conditions`_ system is also included, enabling you to send users to a T&C acceptance page before they
can access the site if you wish. The T&C module is completely optional.

Django Social Profile relies on omab's excellent _django-socialauth: https://github.com/omab/django-social-auth to do
thet actual authentication with the backend providers. If you are just looking for the authentication piece, as opposed
to the UI for customers to use, that module will be all you need. If you are willing to spend a bit of time with the UI,
you can integrate any of the backends that django-socialauth provides (which is extensive).

.. contents:: Table of Contents

Features
--------

This module is meant to be as quick to integrate as possible, and thus extensive customization will likely benefit from
a fork. That said, a number of options are available.

- The core features:
    * _`Login Modal Layer`:
    * _`Self Profile View`:
    * _`Other Profile View`:
    * _`Profile Edit View`:
    * _`Profile Add Auth Type`:
    * _`Profile Delete Auth Type`:
    * _`Delete Account`:

- The Terms and Conditions features:
    * _`Terms and Conditions View`:
    * _`Terms and Conditions Accept`:
    * _`Terms and Conditions Versioning`:
    * _`Terms and Conditions Middleware`:
    * _`Terms and Conditions View Decorator`:


Dependencies
------------

Dependencies that **must** be meet to use the application:

- _django-socialauth: https://github.com/omab/django-social-auth

- python-openid_

- python-oauth2_

- You will need API Keys from Google, Facebook, and Twitter.

Installation
------------

From _pypi: https://pypi.python.org::

    $ pip install django-socialprofile

or::

    $ easy_install django-social-auth

or clone from github_::

    $ git clone git://github.com/cyface/django-socialprofile.git

and add social_auth to PYTHONPATH::

    $ export PYTHONPATH=$PYTHONPATH:$(pwd)/django-socialprofile/

or::

    $ cd django-socialprofile
    $ sudo python setup.py install


Demo App
--------
The socialprofile_demo app is included to quickly let you see how to get a working installation going.

The demo is built as a mobile app using _jQueryMobile:http://jquerymobile.com/ loaded from the jquery CDN.

Take a look at the requirements.txt file in the socialprofile_demo directory for a quick way to use pip to install
all the needed dependencies:

    $ pip install -r requirements.txt

The settings_main.py, and settings_local_template.py files have a working configuration you can crib from.

The templates in the socialprofile/templates directory termsandconditions/templates, and socialprofile_demo/templates
give you a good idea of the kinds of things you will need to do if you want to provide a custom interface.

Configuration
-------------

- Add social_auth and socialprofile to ``PYTHONPATH`` and installed applications::

    INSTALLED_APPS = (
        ...
        'social_auth',
        'socialprofile',
        'termsandconditions',
    )

- All of the configuration for django-socialauth applies to this module, especially the API keys and such.

- You should set up all the redirects for post-authentication:

    # Social Authentication (django-socialauth) Settings
    SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/secure/'
    SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/secure/'
    SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/secure/'

- And set up the redirects for forcing auth on the way to other pages:

    # Core Authentication Settings
    LOGIN_URL          = '/socialprofile/select/'
    LOGIN_REDIRECT_URL = '/secure/'
    LOGIN_ERROR_URL    = '/socialprofile/select/'

- In your urls.py, you need to pull in the socialprofile urls:

    # Social Profiles
    url(r'^socialprofile/', include('socialprofile.urls')),

    # Terms and Conditions
    url(r'^terms/', include('termsandconditions.urls')),

- The django-socialauth urls get pulled in by socialprofile as /socialprofile/socialauth/.

- Setup your backends:

    # Django Socialauth Settings
    SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook', 'google-oauth2', 'twitter')


- Register for your API Keys:

- Google

https://code.google.com/apis/console/

Set the return URL to http://localhost:8000/socialprofile/socialauth/complete/google-oauth2/ for development when you
set up the API key.

- Twitter

https://dev.twitter.com/apps/new

Set the callback URL to http://profile.stepweaver.com/socialprofile/socialauth/complete/twitter/ for development when
you set up the API key.

- Facebook

Facebook is a bit of a pain, since you can only have one URL per API key.

https://developers.facebook.com/apps

Set the site URL http://localhost:8000/ for local development.

Take the keys from your APIs and add them to your settings:

    TWITTER_CONSUMER_KEY         = ''
    TWITTER_CONSUMER_SECRET      = ''
    FACEBOOK_APP_ID              = ''
    FACEBOOK_API_SECRET          = ''
    FACEBOOK_EXTENDED_PERMISSIONS = ['email',]
    GOOGLE_OAUTH2_CLIENT_ID      = ''
    GOOGLE_OAUTH2_CLIENT_SECRET  = ''
    GOOGLE_OAUTH_EXTRA_SCOPE     = ['https://www.googleapis.com/auth/userinfo.profile',]

Note that the extended permissions and such there are typical, you may want to request the ability to post as that user
and so forth.

Views and Layers
^^^^^^^^^^^^^^^^

- `Login Modal Layer`_

The 'socialprofile/select' view provides a login modal that you can use to both force existing users to sign in
as well as to enable new users to select how they want to authenticate to the site.

If you have LOGIN_URL set to '/socialprofile/select/', this will work automatically.

The default template has attributes to make this a nice modal using jQueryMobile, but the HTML is straightforward,
and a custom template should be simple to create.

- `Self Profile View`_

The 'socialprofile/' view lets a user see their own profile. The default template checks to see if they profile is
indeed theirs, and displays an 'edit' button taking them to the 'socialprofile/edit/' view.

This view supports a ?returnTo= parameter to specify a URL path to return to once the user is done. The default template
uses this for the '< Return' button.

- `Other Profile View`_

The 'socialprofile/view/<username>' view lets a user see any profile. You may want to adjust the template to hide any
profile fields that should not be public.

This view supports a ?returnTo= parameter to specify a URL path to return to once the user is done. The default template
uses this for the '< Return' button.

- `Profile Edit View`_

The 'socialprofile/edit/' view lets a user edit their own profile. In typical Django fashion, a GET request to this view
will display the form, while a POST request to this view will try and save the changes.

This view supports a ?returnTo= parameter to specify a URL path to return to once the user is done. The default template
uses this for the 'Cancel' and 'Done' button. When the form returns to the Self Profile View, it passes returnTo.

- `Profile Add Auth Type`_

A user can add an additional social authentication type to their existing profile. If they originally created their
profile using Google auth, then they could add Facebook and Twitter, enabling them to sign in with any of those services
and access the same account.

To do this, just have the customer log in with their new auth type, and django-socialauth will do the rest.

- `Profile Delete Auth Type`_

This is a default feature of django-socialauth, and is available using:

    {% url socialauth_disconnect user_social_auth.provider %}

... in a template.

- `Delete Account`_

It is important to let customers remove their accounts, and the /socialprofile/delete view prompts them to ensure they
really want to delete their account before sending them to /socialprofile/delete/action?confirm=true.

You may want to provide your own function to do this, that perhaps only deactivates their account.

`Terms and Conditions`_
^^^^^^^^^^^^^^^^^^^^^^^

You will need to set up a Terms and Conditions entry in the admin (or via direct DB load) for users to accept if
you want to use the T&C module.

The default Terms and Conditions entry has a slug of 'site-terms'.

If you don't create one, the first time a user is forced to accept the terms, it will create a default entry for you.

- `Terms and Conditions Versioning`_
Note that the versions and dates of T&Cs are important. You can create a new version of a T&C with a future date,
and once that date is in the past, it will force users to accept that new version of the T&Cs.

- `Terms and Conditions Middleware`_
You can force protection of your whole site by using the T&C middleware. Once activated, any attempt to access an
authenticated page will first check to see if the user has accepted the active T&Cs. This can be a performance impact,
so you can also use the _TermsAndConditionsDecorator to protect specific views, or the pipeline setup to only check on
account creation.

    MIDDLEWARE_CLASSES = (
        ...
        'termsandconditions.middleware.TermsAndConditionsRedirectMiddleware',

By default, some pages are excluded from the middleware, you can configure exclusions with these settings:

    ACCEPT_TERMS_PATH = '/terms/accept/'
    TERMS_EXCLUDE_URL_PREFIX_LIST = {'/admin/',})
    TERMS_EXCLUDE_URL_LIST = {'/', '/terms/required/', '/socialprofile/logout/', '/securetoo/'}

TERMS_EXCLUDE_URL_PREFIX_LIST is a list of 'starts with' strings to exclude, while TERMS_EXCLUDE_URL_LIST is a list of
explicit full paths to exclude.

- `Terms and Conditions View Decorator`_
You can protect only specific views with T&Cs using the @terms_required() decorator at the top of a function like this:

    @login_required
    @terms_required
    def terms_required_view(request):
        ...

Note that you can skip @login_required only if you are forcing auth on that view in some other way.

Requiring T&Cs for Anonymous Users is not supported.

- `Terms and Conditions Pipeline`_
You can force T&C acceptance when a new user account is created using the django-socialauth pipeline:

    SOCIAL_AUTH_PIPELINE = (
        'social_auth.backends.pipeline.social.social_auth_user',
        'social_auth.backends.pipeline.associate.associate_by_email',
        'social_auth.backends.pipeline.user.get_username',
        'social_auth.backends.pipeline.user.create_user',
        'social_auth.backends.pipeline.social.associate_user',
        'social_auth.backends.pipeline.social.load_extra_data',
        'social_auth.backends.pipeline.misc.save_status_to_session',
        *'termsandconditions.pipeline.user_accept_terms',*
    )

Note that the configuration above also prevents django-socialauth from updating profile data from the social backends
once a profile is created, due to:

    'social_auth.backends.pipeline.user.update_user_details'

...not being included in the pipeline. This is wise behavior when you are letting users update their own profile details.

This pipeline configuration will send users to the '/terms/accept' page right before sending them on to whatever you
have set SOCIAL_AUTH_NEW_USER_REDIRECT_URL to.  However, it will not, without the middleware or decorators described
above, check that the user has accepted the latest T&Cs before letting them continue on to viewing the site.

You can use the various T&C methods in concert depending on your needs.

