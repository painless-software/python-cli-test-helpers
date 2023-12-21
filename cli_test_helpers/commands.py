"""
Useful commands for writing tests for your CLI tool.
"""

from sys import version_info
from types import SimpleNamespace as Namespace

if version_info < (3, 7):
    from subprocess import PIPE, run
else:
    from subprocess import run

__all__ = []


def shell(command, **kwargs):
    """
    Execute a shell command capturing output and exit code.

    This is a better version of ``os.system()`` that captures output and
    returns a convenient namespace object.
    """
    if version_info < (3, 7):
        completed = run(
            command, shell=True, stdout=PIPE, stderr=PIPE, check=False, **kwargs
        )
    else:
        completed = run(command, shell=True, capture_output=True, check=False, **kwargs)

    return Namespace(
        exit_code=completed.returncode,
        stdout=completed.stdout.decode(),
        stderr=completed.stderr.decode(),
    )
