#!/usr/bin/env python3
"""
Packaging setup for cli-test-helpers
"""

from os.path import abspath, dirname, join
from setuptools import find_packages, setup


def read_file(filename):
    """Get the contents of a file"""
    # pylint: disable=unspecified-encoding
    with open(join(abspath(dirname(__file__)), filename)) as file:
        return file.read()


setup(
    name='cli-test-helpers',
    version='3.1.0',
    author='Peter Bittner',
    author_email='peter@painless.software',
    description='Useful helpers for writing tests for your Python CLI program.',
    long_description=read_file('README.rst'),
    long_description_content_type='text/x-rst',
    url='https://github.com/painless-software/python-cli-test-helpers',
    project_urls={
        'Documentation': 'https://python-cli-test-helpers.readthedocs.io/',
        'Examples': 'https://github.com/painless-software/'
                    'python-cli-test-helpers/tree/main/examples',
    },
    packages=find_packages(exclude=['test*', 'examples']),
    include_package_data=True,
    keywords=['python', 'cli', 'testing', 'helpers'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Testing :: Mocking',
        'Topic :: Software Development :: Testing :: Unit',
    ],
    install_requires=[
        'mock<4; python_version<"3"',
    ],
)
