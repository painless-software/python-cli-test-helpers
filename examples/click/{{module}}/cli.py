"""
Command line interface implementation.
"""
import click

from . import command


@click.command()
@click.version_option()
@click.argument("envvar")
def main(envvar):
    """{{project}}"""
    command.example(envvar)
