from setuptools import setup

readme = open('README.rst').read()

setup(
    name="django-socialprofile",
        version="1.1",
    url='https://github.com/cyface/django-socialprofile',
    license='BSD',
    description="django-socialprofile enables users to manage their user profile built by logging in via a social \
    service such as Google, Twitter, or Facebook. It relies on python-socialauth."
    ,
    author='Tim White',
    author_email='tim@cyface.com',

    packages=['socialprofile',
              'socialprofile.templatetags',
    ],
    long_description=readme,
    include_package_data=True,
    zip_safe=True,
        install_requires=['django>=1.9',
                          'python-social-auth>=0.2.13', ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
