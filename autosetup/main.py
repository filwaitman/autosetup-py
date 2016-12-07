# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from datetime import date
import os

from autosetup import licenses, templates, validators
from autosetup.utils import _write_to_file, _get_value, _first_set, _get_command_args

_LICENSE_CONTENT_MAPPING = {
    'MIT': licenses.MIT,
    'GPL2': licenses.GPL2,
    'GPL3': licenses.GPL3,
    'OTHER': '',
}

_LICENSE_CLASSIFIER_MAPPING = {
    'MIT': '\n        "License :: OSI Approved :: MIT License",',
    'GPL2': '\n        "License :: OSI Approved :: GNU General Public License (GPL)",',
    'GPL3': '\n        "License :: OSI Approved :: GNU General Public License (GPL)",',
    'OTHER': '',
}


def main(
    module_name=None, name=None, version=None, author_name=None, author_email=None,
    cvs_url=None, tests_module=None, requirements=None, tests_requirements=None, readme=None, license=None,
    use_defaults=None, overwrite_all=None, return_values=False

):
    cwd = os.getcwd()
    args = _get_command_args()

    use_defaults = _first_set(use_defaults, args.use_defaults, False)
    overwrite_all = _first_set(overwrite_all, args.overwrite_all, False)

    module_name_initial = _first_set(module_name, args.module_name)
    module_name = _get_value('Module name', initial=module_name_initial, validator=validators.validate_module_name)

    name_initial = _first_set(name, args.name, module_name if use_defaults else None)
    version_initial = _first_set(version, args.version, '0.0.1' if use_defaults else None)
    author_name_initial = _first_set(author_name, args.author_name)
    author_email_initial = _first_set(author_email, args.author_email)
    cvs_url_initial = _first_set(cvs_url, args.cvs_url)
    tests_module_initial = _first_set(tests_module, args.tests_module, 'tests' if use_defaults else None)
    requirements_initial = _first_set(requirements, args.requirements, 'requirements.txt' if use_defaults else None)
    tests_requirements_initial = _first_set(
        tests_requirements, args.tests_requirements, 'requirements_test.txt' if use_defaults else None
    )
    readme_initial = _first_set(readme, args.readme, 'README.rst' if use_defaults else None)
    license_initial = _first_set(license, args.license)

    name = _get_value('Name', initial=name_initial, default=module_name, validator=validators.validate_name)
    version = _get_value('Initial version', initial=version_initial, default='0.0.1')
    author_name = _get_value('Author name', initial=author_name_initial)
    author_email = _get_value('Author email', initial=author_email_initial, validator=validators.validate_email)
    cvs_url = _get_value('CVS (GitHub, Bitbucket) URL', initial=cvs_url_initial, validator=validators.validate_url)
    tests_module = _get_value('Tests module', initial=tests_module_initial, default='tests')
    requirements = _get_value('Requirements file', initial=requirements_initial, default='requirements.txt')
    tests_requirements = _get_value(
        'Tests requirements file', initial=tests_requirements_initial, default='requirements_test.txt'
    )
    readme = _get_value('README file', initial=readme_initial, default='README.rst')
    license = _get_value('License', initial=license_initial, choices=('MIT', 'GPL2', 'GPL3', 'OTHER'))

    final_params = dict(
        module=module_name,
        name=name,
        version=version,
        author_name=author_name,
        author_email=author_email,
        cvs_url=cvs_url,
        tests_module=tests_module,
        requirements=requirements,
        tests_requirements=tests_requirements,
        readme=readme,
        license=license,

        license_classifier=_LICENSE_CLASSIFIER_MAPPING[license],
        year=date.today().year,
        download_url="\n    download_url='{}/tarball/{}'.format(BASE_CVS_URL, VERSION)," if 'github' in cvs_url else ''
    )

    requirements_content = '\n'
    _write_to_file(os.path.join(cwd, requirements), requirements_content, overwrite_all)

    tests_requirements_content = '\n'
    _write_to_file(os.path.join(cwd, tests_requirements), tests_requirements_content, overwrite_all)

    readme_content = name + '\n' + ('=' * len(name)) + '\n'
    _write_to_file(os.path.join(cwd, readme), readme_content, overwrite_all)

    manifest_content = templates.MANIFEST_IN_BASE.format(**final_params).strip() + '\n'
    _write_to_file(os.path.join(cwd, 'MANIFEST.in'), manifest_content, overwrite_all)

    license_content = _LICENSE_CONTENT_MAPPING[license].format(**final_params)
    _write_to_file(os.path.join(cwd, 'LICENSE'), license_content, overwrite_all)

    setup_cfg_content = templates.SETUP_CFG_BASE.format(**final_params).strip() + '\n'
    _write_to_file(os.path.join(cwd, 'setup.cfg'), setup_cfg_content, overwrite_all)

    setup_py_content = templates.SETUP_PY_BASE.format(**final_params).strip() + '\n'
    _write_to_file(os.path.join(cwd, 'setup.py'), setup_py_content, overwrite_all)

    if return_values:
        return final_params  # For testing purposes.

if __name__ == '__main__':
    main()
