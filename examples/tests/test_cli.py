"""
Tests for command line interface (CLI)
"""
import os
import pytest

import foobar.cli


def test_runas_module():
    """
    Can this package be run as a Python module?
    """
    exit_status = os.system('python -m foobar --help')
    assert exit_status == 0


def test_entrypoint():
    """
    Is entrypoint script installed? (setup.py)
    """
    exit_status = os.system('foobar --help')
    assert exit_status == 0


def test_baz_command():
    """
    Is command available?
    """
    exit_status = os.system('foobar baz --help')
    assert exit_status == 0


# NOTE:
# You can continue here, adding all CLI command combinations
# using a non-destructive option, such as --help, to test for
# the availability of the CLI command or option.


def test_cli():
    """
    Does CLI stop execution w/o a command argument?
    """
    with pytest.raises(SystemExit):
        foobar.cli.main()
        pytest.fail("CLI doesn't abort asking for a command argument")
