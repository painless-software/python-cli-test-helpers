"""
Example command module.
"""


def dispatch(file, silent, verbose):
    """An example implementation"""

    with open(file) as textfile:

        if verbose:
            print("Opening text file for reading...")

        content = textfile.read()

        if verbose:
            print("Displaying text file...")

        if not silent:
            print(content)
