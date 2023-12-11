"""
Tests for command line interface (CLI).
"""
from importlib import import_module
from importlib.metadata import version
from os import linesep

from cli_test_helpers import shell
from click.testing import CliRunner

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


def test_usage():
    """
    Does CLI abort w/o arguments, displaying usage instructions?
    """
    runner = CliRunner()
    result = runner.invoke({{module}}.cli.main)

    assert "Usage:" in result.output
    assert result.exit_code != 0


def test_version():
    """
    Does --version display information as expected?
    """
    expected_version = version("{{package}}")
    result = shell("{{package}} --version")

    assert result.stdout == f"{{package}}, version {expected_version}{linesep}"
    assert result.exit_code == 0


def test_example_command():
    """
    Is command available?
    """
    result = shell("{{package}} example --help")
    assert result.exit_code == 0


# NOTE:
# You can continue here, adding all CLI command combinations
# using a non-destructive option, such as --help, to test for
# the availability of the CLI command or option.
