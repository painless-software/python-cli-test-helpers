"""
Useful helpers for writing tests for your Python CLI program.
"""
__author__ = 'Peter Bittner'
__email__ = 'peter@painless.software'
__license__ = 'GPLv3'
__url__ = 'https://github.com/painless-software/python-cli-test-helpers'
__version__ = '2.1.0'

__all__ = [
    'ArgvContext',
    'EnvironContext',
    'shell',
]

from .commands import shell
from .decorators import ArgvContext, EnvironContext
