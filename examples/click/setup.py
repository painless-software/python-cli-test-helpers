"""
Packaging for {{package}}.
"""
from pathlib import Path

from setuptools import find_packages, setup

import {{module}} as package


def read_file(filename):
    """Read a text file and return its contents."""
    project_home = Path(__file__).parent.resolve()
    return (project_home / filename).read_text(encoding="utf-8")


setup(
    name='{{package}}',
    version=package.__version__,
    description=package.__doc__.strip().split('\n', maxsplit=1)[0],
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='{{url}}',
    author='{{author}}',
    author_email='{{email}}',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Networking',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            '{{package}} = {{module}}.cli:main',
        ],
    },
)
