from setuptools import setup

VERSION = '0.0.3'
BASE_CVS_URL = 'http://github.com/filwaitman/autosetup.py'

setup(
    name='autosetup-py',
    packages=['autosetup', ],
    version=VERSION,
    author='Filipe Waitman',
    author_email='filwaitman@gmail.com',
    install_requires=[x.strip() for x in open('requirements.txt').readlines()],
    url=BASE_CVS_URL,
    download_url='{}/tarball/{}'.format(BASE_CVS_URL, VERSION),
    test_suite='tests',
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        'console_scripts': [
            'autosetup-py=autosetup.main:main'
        ]
    }
)
