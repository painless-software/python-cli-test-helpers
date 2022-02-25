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
    old_environ = os.environ
    old_path = os.getenv('PATH')

    assert os.environ == old_environ
    assert os.getenv('PATH') is not None, "Invalid test setup"
    assert os.getenv('FOO') is None, "Invalid test setup"

    with EnvironContext(PATH=None, FOO='my foo value'):
        assert os.getenv('PATH') is None, \
            "os.environ[PATH] wasn't removed by the contextmanager"
        assert os.getenv('FOO') == 'my foo value', \
            "os.environ[FOO] wasn't set by the contextmanager"

    assert os.environ == old_environ, "object os.environ was not restored"
    assert os.getenv('PATH') == old_path, "env var PATH was not restored"
    assert os.getenv('FOO') is None, "env var FOO was not cleared"
