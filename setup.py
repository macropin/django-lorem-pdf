#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup

setup(name='docmk',
    version='0.1.0',
    long_description=open('README.md').read(),
    url='https://github.com/macropin/docmk',
    packages=['docmk',],
    install_requires=['django','django-adlibre',],
    package_data={ 'docmk': ['templates/*',] },
    dependency_links = [
        "https://github.com/adlibre/django-adlibre/tarball/master#egg=django-adlibre"
    ],
)
