"""
An example CLI program
"""
import click

from . import command


@click.group()
@click.version_option()
def main():
    """An example CLI"""


@main.command()
def baz():
    """An example command"""
    command.baz()
