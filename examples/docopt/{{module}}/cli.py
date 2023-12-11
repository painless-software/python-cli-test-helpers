"""{{package}}

{{project}}.

Usage:
  {{package}} (-h | --help | --version)
  {{package}} [-s | --silent] <file>
  {{package}} [-v | --verbose] <file>

Positional arguments:
  file           target file path name

Options:
  -h, --help     show this help message and exit
  -s, --silent   don't show progress output
  -v, --verbose  explain progress verbosely
  --version      show program's version number and exit
"""
from importlib.metadata import version

from docopt import docopt

from . import command


def parse_arguments():
    """Parse and handle CLI arguments."""
    args = docopt(__doc__, version=version("{{package}}"))

    return {
        "file": args["<file>"],
        "silent": args["--silent"],
        "verbose": args["--verbose"],
    }


def main():
    """{{project}}."""
    args = parse_arguments()
    command.dispatch(**args)
