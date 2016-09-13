from setuptools import setup

VERSION = '1.0'
BASE_CVS_URL = 'http://bitbucket.org/waitman/supermodule1'

setup(
    name='yey',
    packages=['supermodule', ],
    version=VERSION,
    author='Filipe Waitman1',
    author_email='filwaitman1@gmail.com',
    install_requires=[x.strip() for x in open('requirements1.txt').readlines()],
    url=BASE_CVS_URL,
    test_suite='tests1',
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
)
