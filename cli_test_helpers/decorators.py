"""
Useful helpers for writing tests for your CLI tool.
"""

import contextlib
import sys
from unittest.mock import patch

__all__ = []


class ArgvContext:
    """
    A simple context manager allowing to temporarily override ``sys.argv``.
    """

    def __init__(self, *new_args):
        self._old = sys.argv
        self.args = type(self._old)(new_args)

    def __enter__(self):
        sys.argv = self.args

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.argv = self._old


class EnvironContext(patch.dict):
    """
    A simple context manager allowing to temporarily set environment values.

    This is syntactic sugar for `unittest.mock.patch.dict`_ as seen in the
    Python documentation, plus allowing to clear single environment variables.

    .. _unittest.mock.patch.dict:
        https://docs.python.org/3/library/unittest.mock.html#patch-dict
    """

    def __init__(self, **kwargs):
        self.clear_variables = [key for key, val in kwargs.items() if val is None]

        for key in self.clear_variables:
            kwargs.pop(key)

        super().__init__("os.environ", **kwargs)

    def __enter__(self):
        super().__enter__()

        for key in self.clear_variables:
            with contextlib.suppress(KeyError):
                self.in_dict.pop(key)
