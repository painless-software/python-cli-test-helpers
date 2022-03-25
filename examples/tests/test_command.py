"""
Tests for the command module
"""
from unittest.mock import patch

import pytest
from cli_test_helpers import ArgvContext, EnvironContext

import foobar.command


@patch('foobar.command.example')
def test_cli_command(mock_command):
    """
    Is the correct code called when invoked via the CLI?
    """
    with ArgvContext('foobar', 'example'), pytest.raises(SystemExit):
        foobar.cli.main()

    assert mock_command.called


def test_fail_without_secret():
    """
    Must fail without a ``SECRET`` environment variable specified
    """
    message_regex = "Environment value SECRET not set."

    with EnvironContext(SECRET=None):
        with pytest.raises(SystemExit, match=message_regex):
            foobar.command.example()
            pytest.fail("CLI doesn't abort with missing SECRET")
