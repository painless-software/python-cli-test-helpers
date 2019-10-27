"""
Example command module
"""
import os


def baz():
    """An example command"""
    try:
        os.environ['SECRET']
    except KeyError:
        SystemExit('Environment value SECRET not set.')
