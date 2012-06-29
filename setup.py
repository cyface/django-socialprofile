import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-socialprofile",
    version = ".1",
    url = 'http://timlwhite.com',
    license = 'GPL',
    description = "django-socialprofile enables users to manage their social profile.",
    long_description = read('README.rst'),

    author = 'Tim White',
    author_email = 'tim@cyface.com',

#    install_requires = ['setuptools', 'django', ],
    
    packages = find_packages(exclude=('socialprofile_demo', )),
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
