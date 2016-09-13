from setuptools import setup

VERSION = '42'
BASE_CVS_URL = 'http://www.google.com'

setup(
    name='namename',
    packages=['supersuper', ],
    version=VERSION,
    author='Hamster Smith',
    author_email='hamster@smith.com',
    install_requires=[x.strip() for x in open('requires.txt').readlines()],
    url=BASE_CVS_URL,
    test_suite='whatever',
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
)
