"""
Example command module.
"""
import os

import click


def example(envvar):
    """An example command."""
    try:
        value = os.environ[envvar]
        click.echo(f"{envvar} = {value}")
    except KeyError:
        msg = f"Environment value {envvar} not set."
        raise SystemExit(msg)
