# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import argparse
import os

from autosetup.compat import input_method


def _confirm(message, default=None):
    post_message = '[y/n]'
    default_answer = None

    if default is not None:
        if default is True:
            default_answer = 'Y'
            post_message = '[Y/n]'
        elif default is False:
            default_answer = 'N'
            post_message = '[y/N]'
        else:
            raise RuntimeError

    answer = None
    while answer not in ('Y', 'N'):
        answer = input_method('{} {}: '.format(message, post_message)).upper()
        if not answer and default_answer:
            answer = default_answer

    return answer == 'Y'


def _write_to_file(file_path, content, force):
    if os.path.exists(file_path) and not force:
        confirm = _confirm('Overwrite {}?'.format(file_path), default=False)
        if not confirm:
            return

    with open(file_path, 'w') as f:
        f.write(content)


def _get_value(message, initial=None, required=True, default=None, validator=None, choices=None):
    value = initial
    first_iteration = True

    post_message = ''
    if choices is not None:
        post_message += ' (one of "{}")'.format('", "'.join(choices))
    if default is not None:
        post_message += ' [default: "{}"]'.format(default)
    prompt_message = '{}{}: '.format(message, post_message)

    while True:
        if first_iteration and initial:
            value = initial
            first_iteration = False

        else:
            value = input_method(prompt_message).strip()

        if not value:
            if default is not None:
                value = default
            elif not required:
                value = ''
            else:
                continue

        if validator:
            if validator(value):
                return value
        elif choices:
            if value in choices:
                return value
        else:
            return value


def _first_set(*values):
    for value in values:
        if value is not None:
            return value


def _get_command_args():
    parser = argparse.ArgumentParser(description='autosetup-py')
    parser.add_argument('--module', dest='module_name', help='Module name')
    parser.add_argument('--name', dest='name', help='Name [default: module name]')
    parser.add_argument('--version', dest='version', help='Initial version [default: "0.0.1"]')
    parser.add_argument('--author_name', dest='author_name', help="Author name")
    parser.add_argument('--author_email', dest='author_email', help="Author email")
    parser.add_argument('--cvs_url', dest='cvs_url', help="CVS (GitHub, Bitbucket) URL")
    parser.add_argument('--tests_module', dest='tests_module', help='Tests module [default: "tests"]')
    parser.add_argument('--requirements', dest='requirements', help='Requirements file [default: "requirements.txt"]')
    parser.add_argument(
        '--tests_requirements', dest='tests_requirements',
        help='Tests requirements file [default: "requirements_test.txt"]'
    )
    parser.add_argument('--readme', dest='readme', help='README file [default: "README.rst"]')
    parser.add_argument('--license', dest='license', default='', help='License ("MIT", "GPL2, "GPL3", or "OTHER")')
    parser.add_argument('--use-defaults', dest='use_defaults', action='store_true', default=False)
    parser.add_argument('--overwrite-all', dest='overwrite_all', action='store_true', default=False)
    return parser.parse_args()
