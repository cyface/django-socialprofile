from setuptools import setup

readme = open('README.rst').read()

setup(
    name="django-socialprofile",
    version="1.2",
    url='https://github.com/cyface/django-socialprofile',
    license='BSD',
    description="django-socialprofile enables users to manage their user profile built by logging in via a social \
    service such as Google, Twitter, or Facebook. It relies on python-socialauth.",
    author='Tim White',
    author_email='tim@cyface.com',
    packages=[
        'socialprofile',
        'socialprofile.templatetags',
    ],
    long_description=readme,
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'django>=1.8.3',
        'python-social-auth>=0.2.19',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
