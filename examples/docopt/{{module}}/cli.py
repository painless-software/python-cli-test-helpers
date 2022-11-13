"""{{package}}

{{project}}.

Usage:
  {{package}} (-h | --help | --version)
  {{package}} [-s | --silent] <file>
  {{package}} [-v | --verbose] <file>

Positional arguments:
  file           target file path name

Optional arguments:
  -h, --help     show this help message and exit
  -s, --silent   don't show progress output
  -v, --verbose  explain progress verbosely
  --version      show program's version number and exit
"""
from docopt import docopt

from . import __version__
from . import command


def parse_arguments():
    """
    Parse and handle CLI arguments
    """
    args = docopt(__doc__, version=__version__)

    return dict(
        file=args['<file>'],
        silent=args['-s'] or args['--silent'],
        verbose=args['-v'] or args['--verbose'],
    )


def main():
    """{{project}}"""
    args = parse_arguments()

    command.process(**args)
