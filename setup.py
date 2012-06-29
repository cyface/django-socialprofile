import os
import sys

from setuptools import setup, find_packages

def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    
    Taken from Django's setup.py
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)



def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# Taken from Django's setup.py
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != "":
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk("socialprofile"):
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])    

for dirpath, dirnames, filenames in os.walk("termsandconditions"):
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]]) 
         

setup(
    name = "django-socialprofile",
    version = ".1",
    url = 'http://timlwhite.com',
    license = 'GPL',
    description = "django-socialprofile enables users to manage their social profile.",
    long_description = read('README.rst'),

    author = 'Tim White',
    author_email = 'tim@cyface.com',

    zip_safe = False,
    packages = packages,
    data_files = data_files,
    
    install_requires = ['setuptools', 'django', ],

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
