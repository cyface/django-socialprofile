from setuptools import setup, find_packages

setup(
    name="django-socialprofile",
    version="0.1.6",
    url='http://timlwhite.com',
    license='BSD',
    description="django-socialprofile enables users to manage their user profile built by logging in via a social service such as Google, Twitter, or Facebook. It relies on django-socialauth."
    ,
    long_description=open('README.rst').read(),

    author='Tim White',
    author_email='tim@cyface.com',

    packages=['socialprofile',
              'socialprofile.templatetags',
              ],
    include_package_data=True,
    zip_safe=True,

    install_requires=['django>=1.4',
                      'django-social-auth>=0.7.0', ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        ]
)
