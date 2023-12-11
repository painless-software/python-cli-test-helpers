"""
Command line interface implementation.
"""
import argparse
from importlib.metadata import version

from . import command


def parse_arguments():
    """Parse and handle CLI arguments."""
    __version__ = version("{{package}}")

    parser = argparse.ArgumentParser(description="{{project}}")

    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument("action", choices=["get", "set"])
    parser.add_argument("envvar", nargs="?", default="SECRET",
                        help="default: %(default)s")

    return parser.parse_args()


def dispatch(args):
    """Execute functionality requested through the CLI."""
    if args.action == "get":
        command.example(args)
    else:
        raise NotImplementedError(args.action)


def main():
    """{{project}}."""
    args = parse_arguments()
    dispatch(args)
