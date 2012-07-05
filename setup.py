from setuptools import setup, find_packages

setup(
    name = "django-socialprofile",
    version = ".1",
    url = 'http://timlwhite.com',
    license = 'GPL',
    description = "django-socialprofile enables users to manage their user profile built by logging in via a social service such as Google, Twitter, or Facebook. It relies on django-socialauth.",
    long_description = open('README.rst').read(),

    author = 'Tim White',
    author_email = 'tim@cyface.com',
    
    packages = find_packages(exclude=('socialprofile_demo', 'tests', 'devscripts' )),
    include_package_data = True,
    zip_safe = False,

    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
