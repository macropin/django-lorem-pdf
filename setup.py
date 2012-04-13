#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup

setup(name='lorem_pdf',
    version='0.1.1',
    long_description=open('README.md').read(),
    url='https://github.com/macropin/django-lorem-pdf',
    packages=['lorem_pdf',],
    install_requires=['django','django-adlibre',],
    package_data={ 'lorem_pdf': ['templates/*',] },
    dependency_links = [
        "https://github.com/adlibre/django-adlibre/tarball/master#egg=django-adlibre"
    ],
)
