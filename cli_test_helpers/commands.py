"""
Useful commands for writing tests for your CLI tool
"""
from argparse import Namespace
from subprocess import run

__all__ = []


def shell(command, **kwargs):
    """
    A better version of ``os.system()`` that captures output and returns a
    convenient namespace object.
    """
    # pylint: disable=subprocess-run-check
    completed = run(command, shell=True, capture_output=True, **kwargs)

    return Namespace(
        status=completed.returncode,
        stdout=completed.stdout.decode(),
        stderr=completed.stderr.decode(),
    )
