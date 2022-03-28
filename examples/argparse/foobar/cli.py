"""
An example CLI program.
"""
import argparse

from . import __version__, command


def parse_arguments():
    """
    Parse and handle CLI arguments
    """
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('action', choices=['get', 'set'])
    parser.add_argument('envvar', nargs='?', default='SECRET',
                        help='default: %(default)s')

    args = parser.parse_args()
    return args


def main():
    """An example CLI"""
    args = parse_arguments()

    if args.action == 'get':
        command.example(args)
    else:
        raise NotImplementedError(args.action)
