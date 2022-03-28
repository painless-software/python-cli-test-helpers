"""
An example CLI program
"""
import click

from . import command


@click.command()
@click.version_option()
@click.argument('envvar')
def main(envvar):
    """An example CLI"""
    command.example(envvar)
