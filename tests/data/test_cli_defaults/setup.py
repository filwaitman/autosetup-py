from setuptools import setup

VERSION = '0.0.1'
BASE_CVS_URL = 'http://bitbucket.org/waitman/supermodule1'

setup(
    name='supermodule',
    packages=['supermodule', ],
    version=VERSION,
    author='Filipe Waitman1',
    author_email='filwaitman1@gmail.com',
    install_requires=[x.strip() for x in open('requirements.txt').readlines()],
    url=BASE_CVS_URL,
    test_suite='tests',
    tests_require=[x.strip() for x in open('requirements_test.txt').readlines()],
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
)
