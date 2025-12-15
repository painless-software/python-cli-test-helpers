"""
Useful helpers for writing tests for your CLI tool.
"""

import contextlib
import os
import sys
from tempfile import TemporaryDirectory
from unittest.mock import patch

from .mixins import LoggingIsolationMixin

__all__ = []


class ArgvContext(LoggingIsolationMixin):
    """
    A simple context manager allowing to temporarily override ``sys.argv``.

    Use it to mimic the command line arguments of the CLI application.
    Note that the first argument (index ``0``) is always the script or
    application name.
    """

    def __init__(self, *new_args):
        self._old = sys.argv
        self.args = type(self._old)(new_args)

    def __enter__(self):
        super().__enter__()
        sys.argv = self.args
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.argv = self._old
        super().__exit__(exc_type, exc_val, exc_tb)


class EnvironContext(LoggingIsolationMixin, patch.dict):
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

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return super().__exit__(exc_type, exc_val, exc_tb)


class RandomDirectoryContext(LoggingIsolationMixin, TemporaryDirectory):
    """
    Change the execution directory to a random location, temporarily.

    Keyword arguments are optional and identical to the ones of
    `tempfile.TemporaryDirectory`_ of the Python standard library.

    .. _tempfile.TemporaryDirectory:
        https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryDirectory
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __enter__(self):
        """Create a temporary directory and ``cd`` into it."""
        super().__enter__()

        self.__prev_dir = os.getcwd()
        os.chdir(self.name)
        return os.getcwd()

    def __exit__(self, exc_type, exc_value, traceback):
        """Return to the original directory before execution."""
        os.chdir(self.__prev_dir)
        return super().__exit__(exc_type, exc_value, traceback)
