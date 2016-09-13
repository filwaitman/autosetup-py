# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import keyword
import re

from autosetup.compat import urlparse


def validate_module_name(value):
    if not value or not value.strip():
        return False
    value = value.strip()

    return all([
        value.isalnum(),
        value not in keyword.kwlist,
        value[0].isalpha(),
        value not in ('True', 'False', 'None'),
    ])


def validate_name(value):
    if not value or not value.strip():
        return False
    value = value.strip()

    return all([
        re.match('^[\w-]+$', value),
        value[0].isalpha(),
        value not in ('True', 'False', 'None'),
    ])


def validate_email(value):
    if not value or not value.strip():
        return False
    value = value.strip()

    return bool(re.match('^\w+[\w\-\.]+\w+@\w+[\w\-]+\w+\.\w+[\w\-\.]+$', value))  # TODO: beter validation.


def validate_url(value):
    if not value or not value.strip():
        return False
    value = value.strip()

    parsed_url = urlparse(value)
    return bool(parsed_url.netloc) and bool(parsed_url.scheme)
