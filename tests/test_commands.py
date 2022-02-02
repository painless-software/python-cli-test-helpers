"""
Tests for our cli test commands
"""
from os import linesep

from cli_test_helpers import shell


def test_shell_output():
    """
    Does shell run a shell command and capture its output?
    """
    message = "Git CLI Helpers"

    result = shell("echo " + message)

    assert result.exit_code == 0, "Command execution reported as failure"
    assert result.stdout == message + linesep, "Unexpected output of shell"


def test_shell_fails_gracefully():
    """
    An erroneous command execution throws no exception but sets the exit
    code to nonzero.
    """
    result = shell("some-invalid-command-that-doesnt-exist")

    assert result.exit_code != 0, "Command execution not reported as failure"
