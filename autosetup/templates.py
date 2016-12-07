# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

SETUP_PY_BASE = '''
from setuptools import setup

VERSION = '{version}'
BASE_CVS_URL = '{cvs_url}'

setup(
    name='{name}',
    packages=['{module}', ],
    version=VERSION,
    author='{author_name}',
    author_email='{author_email}',
    install_requires=[x.strip() for x in open('{requirements}').readlines()],
    url=BASE_CVS_URL,{download_url}
    test_suite='{tests_module}',
    tests_require=[x.strip() for x in open('{tests_requirements}').readlines()],
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: OS Independent",{license_classifier}
    ],
)
'''

SETUP_CFG_BASE = '''
[metadata]
description-file = {readme}
'''

MANIFEST_IN_BASE = '''
include *.txt
include {readme}
include {tests_module}/*
'''
