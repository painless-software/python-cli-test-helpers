"""
Tests for command line interface (CLI)
"""
from importlib.metadata import version
from os import linesep

import foobar.cli
import pytest

from cli_test_helpers import ArgvContext, shell


def test_runas_module():
    """
    Can this package be run as a Python module?
    """
    result = shell('python -m foobar --help')
    assert result.exit_code == 0


def test_entrypoint():
    """
    Is entrypoint script installed? (setup.py)
    """
    result = shell('foobar --help')
    assert result.exit_code == 0


def test_version():
    """
    Does --version display information as expected?
    """
    expected_version = version('foobar')
    result = shell('foobar --version')

    assert result.stdout == f"{expected_version}{linesep}"
    assert result.exit_code == 0


def test_get_action():
    """
    Is action argument available?
    """
    with ArgvContext('foobar', 'get'):
        args = foobar.cli.parse_arguments()

    assert args.action == 'get'


def test_set_action():
    """
    Is action argument available?
    """
    with ArgvContext('foobar', 'set'):
        args = foobar.cli.parse_arguments()

    assert args.action == 'set'


# NOTE:
# You can continue here, adding all CLI action and option combinations
# using a non-destructive option, such as --help, to test for the
# availability of the CLI command or option.


def test_cli():
    """
    Does CLI stop execution w/o a command argument?
    """
    with pytest.raises(SystemExit):
        foobar.cli.main()
        pytest.fail("CLI doesn't abort asking for a command argument")
