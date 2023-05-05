"""
Example command module.
"""
from pathlib import Path


def dispatch(file, silent, verbose):
    """An example implementation"""
    try:
        with Path(file).open() as textfile:

            if verbose:
                print("Opening text file for reading...")

            content = textfile.read()

            if verbose:
                print("Displaying text file...")

            if not silent:
                print(content)
    except FileNotFoundError as err:
        raise SystemExit(err)
