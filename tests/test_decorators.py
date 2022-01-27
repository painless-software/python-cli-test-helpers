"""
Tests for our tests helpers  8-}
"""
import os
import sys

from cli_test_helpers import ArgvContext, EnvironContext


def test_argv_context():
    """
    Does ArgvContext set new argvs and reset old ones correctly?
    """
    old = sys.argv
    new = ["Alice", "Bob", "Chris", "Daisy"]

    assert sys.argv == old

    with ArgvContext(*new):
        assert sys.argv == new, \
            "sys.argv wasn't correctly changed by the contextmanager"

    assert sys.argv == old, "sys.argv wasn't correctly reset"


def test_environ_context():
    """
    Does EnvironContext set new environ values and reset old ones correctly?
    """
    old = os.environ
    new = {'PATH': None, 'FOO': 'my foo value'}

    assert os.environ == old
    assert os.environ.get('PATH'), "Invalid test setup"
    assert not os.environ.get('FOO'), "Invalid test setup"

    with EnvironContext(**new):
        assert not os.environ.get('PATH'), \
            "os.environ[PATH] wasn't removed by the contextmanager"
        assert os.environ['FOO'] == new['FOO'], \
            "os.environ[FOO] wasn't set by the contextmanager"

    assert os.environ == old, "os.environ wasn't correctly reset"
