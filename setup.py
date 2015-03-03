#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import demo_django_app
version = demo_django_app.__version__

setup(
    name='demo_django_app',
    version=version,
    author="yanchao",
    author_email='yanchao727@gmail.com',
    packages=[
        'demo_django_app',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.4',
    ],
    zip_safe=False,
    scripts=['demo_django_app/manage.py'],
)
