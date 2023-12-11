"""
Tests for command line interface (CLI).
"""
from importlib import import_module
from importlib.metadata import version
from os import linesep
from unittest.mock import patch

import pytest
from cli_test_helpers import ArgvContext, shell

import {{module}}.cli


def test_main_module():
    """
    Exercise (most of) the code in the ``__main__`` module.
    """
    import_module("{{module}}.__main__")


def test_runas_module():
    """
    Can this package be run as a Python module?
    """
    result = shell("python -m {{module}} --help")
    assert result.exit_code == 0


def test_entrypoint():
    """
    Is entrypoint script installed? (setup.py)
    """
    result = shell("{{package}} --help")
    assert result.exit_code == 0


@patch("{{module}}.command.dispatch")
def test_usage(mock_dispatch):
    """
    Does CLI abort w/o arguments, displaying usage instructions?
    """
    with ArgvContext("{{package}}"), pytest.raises(SystemExit):
        {{module}}.cli.main()

    assert not mock_dispatch.called, "CLI should stop execution"

    result = shell("{{package}}")

    assert "Usage:" in result.stderr


def test_version():
    """
    Does --version display information as expected?
    """
    expected_version = version("{{package}}")
    result = shell("{{package}} --version")

    assert result.stdout == f"{expected_version}{linesep}"
    assert result.exit_code == 0


def test_file_argument():
    """
    Is the positional parameter available?
    """
    result = shell("{{package}} myfile --help")
    assert result.exit_code == 0


# NOTE:
# You can continue here, adding all CLI action and option combinations
# using a non-destructive option, such as --help, to test for the
# availability of the CLI command or option.


@pytest.mark.parametrize(("option", "silent", "verbose"), [
    ("-s", True, False),
    ("-v", False, True),
    ("--silent", True, False),
    ("--verbose", False, True),
])
def test_options(option, silent, verbose):
    """
    Is the (-s | --silent) and (-v | --verbose) option evaluated correctly?
    """
    with ArgvContext("{{package}}", "myfile", option):
        args = {{module}}.cli.parse_arguments()

    assert args["file"] == "myfile"
    assert args["silent"] == silent
    assert args["verbose"] == verbose
