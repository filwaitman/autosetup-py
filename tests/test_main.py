# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from collections import OrderedDict
import os
import unittest

import mock

from autosetup.main import main


class MainTestCase(unittest.TestCase):
    def setUp(self):
        super(MainTestCase, self).setUp()

        self.arguments = OrderedDict()
        self.arguments['module_name'] = 'supermodule'
        self.arguments['name'] = 'yey'
        self.arguments['version'] = '1.0'
        self.arguments['author_name'] = 'Filipe Waitman1'
        self.arguments['author_email'] = 'filwaitman1@gmail.com'
        self.arguments['cvs_url'] = 'http://bitbucket.org/waitman/supermodule1'
        self.arguments['tests_module'] = 'tests1'
        self.arguments['requirements'] = 'requirements1.txt'
        self.arguments['tests_requirements'] = 'requirements_test.txt'
        self.arguments['readme'] = 'README1.rst'
        self.arguments['license'] = 'GPL3'

        self._write_to_file_patched = mock.patch('autosetup.main._write_to_file')
        self.write_to_file_patched = self._write_to_file_patched.start()

        self._input_method_patched = mock.patch('autosetup.utils.input_method')
        self.input_method_patched = self._input_method_patched.start()

        self.args_mock = mock.Mock()
        self.args_mock.configure_mock(
            module_name=None,
            name=None,
            version=None,
            author_name=None,
            author_email=None,
            cvs_url=None,
            tests_module=None,
            requirements=None,
            tests_requirements=None,
            readme=None,
            license=None,
            use_defaults=False,
            overwrite_all=False,
        )
        self._get_command_args_patched = mock.patch('autosetup.main._get_command_args', return_value=self.args_mock)
        self.get_command_args_patched = self._get_command_args_patched.start()
        self.get_command_args_patched.configure_mock()

    def tearDown(self):
        self._write_to_file_patched.stop()
        self._input_method_patched.stop()
        self._get_command_args_patched.stop()

        super(MainTestCase, self).tearDown()

    def assertFileContents(self, path_name, requirements_path, readme_path):
        current_dir = os.path.dirname(os.path.abspath(__file__))

        setup_cfg = open(os.path.join(current_dir, 'data', path_name, 'setup.cfg')).read()
        self.write_to_file_patched.assert_any_call(mock.ANY, setup_cfg, mock.ANY)

        manifest_in = open(os.path.join(current_dir, 'data', path_name, 'MANIFEST.in')).read()
        self.write_to_file_patched.assert_any_call(mock.ANY, manifest_in, mock.ANY)

        license = open(os.path.join(current_dir, 'data', path_name, 'LICENSE')).read()
        self.write_to_file_patched.assert_any_call(mock.ANY, license, mock.ANY)

        requirements = open(os.path.join(current_dir, 'data', path_name, requirements_path)).read()
        self.write_to_file_patched.assert_any_call(mock.ANY, requirements, mock.ANY)

        readme = open(os.path.join(current_dir, 'data', path_name, readme_path)).read()
        self.write_to_file_patched.assert_any_call(mock.ANY, readme, mock.ANY)

        setup_py = open(os.path.join(current_dir, 'data', path_name, 'setup.py')).read()
        self.write_to_file_patched.assert_any_call(mock.ANY, setup_py, mock.ANY)

    def test_cli_common(self):
        self.input_method_patched.side_effect = self.arguments.values()

        result = main(return_values=True)

        self.assertEquals(result['module'], self.arguments['module_name'])
        self.assertEquals(result['name'], self.arguments['name'])
        self.assertEquals(result['version'], self.arguments['version'])
        self.assertEquals(result['author_name'], self.arguments['author_name'])
        self.assertEquals(result['author_email'], self.arguments['author_email'])
        self.assertEquals(result['cvs_url'], self.arguments['cvs_url'])
        self.assertEquals(result['tests_module'], self.arguments['tests_module'])
        self.assertEquals(result['requirements'], self.arguments['requirements'])
        self.assertEquals(result['tests_requirements'], self.arguments['tests_requirements'])
        self.assertEquals(result['readme'], self.arguments['readme'])
        self.assertEquals(result['license'], self.arguments['license'])

        self.assertFileContents('test_cli_common', 'requirements1.txt', 'README1.rst')

    def test_cli_license_other(self):
        arguments = self.arguments.copy()
        arguments['license'] = 'OTHER'
        self.input_method_patched.side_effect = arguments.values()

        result = main(return_values=True)

        self.assertEquals(result['module'], self.arguments['module_name'])
        self.assertEquals(result['name'], self.arguments['name'])
        self.assertEquals(result['version'], self.arguments['version'])
        self.assertEquals(result['author_name'], self.arguments['author_name'])
        self.assertEquals(result['author_email'], self.arguments['author_email'])
        self.assertEquals(result['cvs_url'], self.arguments['cvs_url'])
        self.assertEquals(result['tests_module'], self.arguments['tests_module'])
        self.assertEquals(result['requirements'], self.arguments['requirements'])
        self.assertEquals(result['readme'], self.arguments['readme'])
        self.assertEquals(result['license'], 'OTHER')
        self.assertEquals(result['license_classifier'], '')

        self.assertFileContents('test_cli_license_other', 'requirements1.txt', 'README1.rst')

    def test_cli_defaults(self):
        arguments = self.arguments.copy()
        arguments['name'] = ''
        arguments['version'] = ''
        arguments['tests_module'] = ''
        arguments['requirements'] = ''
        arguments['readme'] = ''
        self.args_mock.use_defaults = True

        self.input_method_patched.side_effect = arguments.values()

        result = main(return_values=True)

        self.assertEquals(result['name'], self.arguments['module_name'])
        self.assertEquals(result['version'], '0.0.1')
        self.assertEquals(result['tests_module'], 'tests')
        self.assertEquals(result['requirements'], 'requirements.txt')
        self.assertEquals(result['readme'], 'README.rst')

        self.assertEquals(result['module'], self.arguments['module_name'])
        self.assertEquals(result['author_name'], self.arguments['author_name'])
        self.assertEquals(result['author_email'], self.arguments['author_email'])
        self.assertEquals(result['cvs_url'], self.arguments['cvs_url'])
        self.assertEquals(result['license'], self.arguments['license'])

        self.assertFileContents('test_cli_defaults', 'requirements.txt', 'README.rst')

    def test_cli_params_being_passed(self):
        args_mock = mock.Mock()
        args_mock.configure_mock(
            module_name='supersuper',
            name='namename',
            version='42',
            author_name='Hamster Smith',
            author_email='hamster@smith.com',
            cvs_url='http://www.google.com',
            tests_module='whatever',
            requirements='requires.txt',
            tests_requirements='requirements_test.txt',
            readme='RTFM',
            license='GPL3',
            use_defaults=False,
            overwrite_all=False,
        )
        self.get_command_args_patched.return_value = args_mock

        result = main(return_values=True)

        self.assertEquals(result['module'], 'supersuper')
        self.assertEquals(result['name'], 'namename')
        self.assertEquals(result['version'], '42')
        self.assertEquals(result['author_name'], 'Hamster Smith')
        self.assertEquals(result['author_email'], 'hamster@smith.com')
        self.assertEquals(result['cvs_url'], 'http://www.google.com')
        self.assertEquals(result['tests_module'], 'whatever')
        self.assertEquals(result['requirements'], 'requires.txt')
        self.assertEquals(result['readme'], 'RTFM')
        self.assertEquals(result['license'], 'GPL3')

        self.assertFileContents('test_cli_params_being_passed', 'requires.txt', 'RTFM')

    def test_main_params_being_passed(self):
        result = main(
            module_name='supersuper',
            name='namename',
            version='42',
            author_name='Hamster Smith',
            author_email='hamster@smith.com',
            cvs_url='http://www.google.com',
            tests_module='whatever',
            requirements='requires.txt',
            tests_requirements='requirements_test.txt',
            readme='RTFM',
            license='GPL3',
            return_values=True
        )

        self.assertEquals(result['module'], 'supersuper')
        self.assertEquals(result['name'], 'namename')
        self.assertEquals(result['version'], '42')
        self.assertEquals(result['author_name'], 'Hamster Smith')
        self.assertEquals(result['author_email'], 'hamster@smith.com')
        self.assertEquals(result['cvs_url'], 'http://www.google.com')
        self.assertEquals(result['tests_module'], 'whatever')
        self.assertEquals(result['requirements'], 'requires.txt')
        self.assertEquals(result['readme'], 'RTFM')
        self.assertEquals(result['license'], 'GPL3')

        self.assertFileContents('test_main_params_being_passed', 'requires.txt', 'RTFM')
