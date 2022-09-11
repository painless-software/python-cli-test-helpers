"""
Packaging for example CLI tool
"""
from pathlib import Path

import foobar as package
from setuptools import find_packages, setup


def read_file(filename):
    """Read a text file and return its contents."""
    project_home = Path(__file__).parent.resolve()
    file_path = project_home / filename
    return file_path.read_text(encoding="utf-8")


setup(
    name='foobar',
    version=package.__version__,
    description=package.__doc__.strip().split('\n', maxsplit=1)[0],
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://example.com/',
    author='Foo Bar',
    author_email='foo.bar@example.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Networking',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'docopt-ng',
    ],
    entry_points={
        'console_scripts': [
            'foobar = foobar.cli:main',
        ],
    },
)
