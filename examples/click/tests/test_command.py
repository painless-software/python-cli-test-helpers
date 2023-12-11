"""
Tests for the command module.
"""
from unittest.mock import patch

import pytest
from cli_test_helpers import ArgvContext, EnvironContext

import {{module}}


@patch("{{module}}.command.example")
def test_cli_command(mock_command):
    """
    Is the correct code called when invoked via the CLI?
    """
    with ArgvContext("{{package}}", "example"), pytest.raises(SystemExit):
        {{module}}.cli.main()

    assert mock_command.called


def test_fail_without_secret():
    """
    Must fail without a ``SECRET`` environment variable specified
    """
    message_regex = "Environment value SECRET not set."

    with EnvironContext(SECRET=None), pytest.raises(SystemExit, match=message_regex):
        {{module}}.command.example("SECRET")
