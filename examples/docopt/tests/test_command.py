"""
Tests for the command module
"""
from unittest.mock import patch

import foobar

from cli_test_helpers import ArgvContext


@patch('foobar.command.process')
def test_process_is_called(mock_command):
    """
    Is the correct code called when invoked via the CLI?
    """
    with ArgvContext('foobar', 'myfile', '-v'):
        foobar.cli.main()

    assert mock_command.called
    assert mock_command.call_args.kwargs == {
        'file': 'myfile',
        'silent': False,
        'verbose': True,
    }


@patch('foobar.command.print')
@patch('foobar.command.open')
def test_process_business_logic(mock_openfile, mock_print):
    """
    Walk the code of the process function.
    """
    foobar.command.process(file='myfile', silent=False, verbose=True)

    assert mock_openfile.called
    assert mock_print.call_count == 3, \
        "Expected 2x for --verbose, 1x for not --silent"
