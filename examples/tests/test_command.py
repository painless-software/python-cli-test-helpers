"""
Tests for the command module
"""
import pytest

from cli_test_helpers import ArgvContext, EnvironContext
from unittest.mock import patch

import foobar.command


@patch('foobar.command.baz')
def test_cli_command(mock_command):
    """
    Is the correct code called when invoked via the CLI?
    """
    with ArgvContext('foobar', 'baz'):
        foobar.command.baz()

    assert mock_command.call_count == 1


def test_fail_without_secret():
    """
    Must fail without a ``SECRET`` environment variable specified
    """
    message = "Environment value SECRET not set."

    with EnvironContext(SECRET=None):
        with pytest.raises(SystemExit, match=message):
            foobar.command.baz()
            pytest.fail("CLI doesn't abort with missing SECRET")
