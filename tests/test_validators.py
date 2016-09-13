# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import unittest

from autosetup.validators import validate_module_name, validate_name, validate_email, validate_url


class ValidateModuleNameTestCase(unittest.TestCase):
    def test_regular_chars(self):
        self.assertTrue(validate_module_name('potato'))
        self.assertTrue(validate_module_name('CrazyCapitalLETTER'))
        self.assertTrue(validate_module_name('z'))

    def test_numbers(self):
        self.assertTrue(validate_module_name('area51'))
        self.assertTrue(validate_module_name('hero2vilain'))

        self.assertFalse(validate_module_name('42isthwanswer'))
        self.assertFalse(validate_module_name('666'))

    def test_empty(self):
        self.assertFalse(validate_module_name(''))
        self.assertFalse(validate_module_name('     '))

    def test_reserved_keywords(self):
        self.assertFalse(validate_module_name('for'))
        self.assertFalse(validate_module_name('if'))

    def test_special_chars(self):
        self.assertFalse(validate_module_name('money-o-rama'))
        self.assertFalse(validate_module_name('ImThe#1'))
        self.assertFalse(validate_module_name('Supercool!'))

    def test_builtins(self):
        # Although I disagree you actually *can* override those ones.
        self.assertTrue(validate_module_name('AssertionError'))
        self.assertTrue(validate_module_name('zip'))

    def test_restricted_builtins(self):
        self.assertFalse(validate_module_name('True'))
        self.assertFalse(validate_module_name('False'))
        self.assertFalse(validate_module_name('None'))


class ValidateNameTestCase(unittest.TestCase):
    def test_regular_chars(self):
        self.assertTrue(validate_name('potato'))
        self.assertTrue(validate_name('CrazyCapitalLETTER'))
        self.assertTrue(validate_name('z'))

    def test_numbers(self):
        self.assertTrue(validate_name('area51'))
        self.assertTrue(validate_name('hero2vilain'))

        self.assertFalse(validate_name('42isthwanswer'))
        self.assertFalse(validate_name('666'))

    def test_empty(self):
        self.assertFalse(validate_name(''))
        self.assertFalse(validate_name('     '))

    def test_reserved_keywords(self):
        self.assertTrue(validate_name('for'))  # No reserved words since this is just the name.
        self.assertTrue(validate_name('if'))  # No reserved words since this is just the name.

    def test_special_chars(self):
        self.assertTrue(validate_name('money-o-rama'))

        self.assertFalse(validate_name('ImThe#1'))
        self.assertFalse(validate_name('Supercool!'))

    def test_builtins(self):
        self.assertTrue(validate_name('AssertionError'))
        self.assertTrue(validate_name('zip'))

    def test_restricted_builtins(self):
        self.assertFalse(validate_name('True'))
        self.assertFalse(validate_name('False'))
        self.assertFalse(validate_name('None'))


class ValidateEmailTestCase(unittest.TestCase):
    def test_common(self):
        self.assertTrue(validate_email('hamster@sloth.com'))
        self.assertTrue(validate_email('HAMSter@sloth.co.nz'))
        self.assertTrue(validate_email('hamster1995x0x0@sloth.com'))
        self.assertTrue(validate_email('hams.ter@sloth.com'))
        self.assertTrue(validate_email('hamster-king@sloth.com'))

    def test_empty(self):
        self.assertFalse(validate_email(''))
        self.assertFalse(validate_email('     '))

    def test_malformed_emails(self):
        self.assertFalse(validate_email('hamsterslothcom'))
        self.assertFalse(validate_email('hamster@slothcom'))
        self.assertFalse(validate_email('hamster@sloth'))
        self.assertFalse(validate_email('hamster@'))
        self.assertFalse(validate_email('@sloth.com'))
        self.assertFalse(validate_email('hamster'))
        self.assertFalse(validate_email('hamster@@sloth.com'))
        self.assertFalse(validate_email('hamster@sloth..com'))
        self.assertFalse(validate_email('hamster.@sloth.com'))
        self.assertFalse(validate_email('hamster@.sloth.com'))
        self.assertFalse(validate_email('hamster@sloth.-com'))
        self.assertFalse(validate_email('hamster-@sloth.com'))
        self.assertFalse(validate_email('hamster@-sloth.com'))


class ValidateUrlTestCase(unittest.TestCase):
    def test_common(self):
        self.assertTrue(validate_url('http://www.google.com'))
        self.assertTrue(validate_url('https://youtube.com/something/else'))

    def test_empty(self):
        self.assertFalse(validate_url(''))
        self.assertFalse(validate_url('     '))

    def test_malformed_emails(self):
        self.assertFalse(validate_url('hamster'))
        self.assertFalse(validate_url('hamster.com'))
        self.assertFalse(validate_url('http'))
        self.assertFalse(validate_url('http://'))
