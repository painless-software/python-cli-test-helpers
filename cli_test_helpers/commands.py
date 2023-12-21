"""
Useful commands for writing tests for your CLI tool.
"""

from subprocess import run
from types import SimpleNamespace as Namespace

__all__ = []


def shell(command, **kwargs):
    """
    Execute a shell command capturing output and exit code.

    This is a better version of ``os.system()`` that captures output and
    returns a convenient namespace object.
    """
    completed = run(command, shell=True, capture_output=True, check=False, **kwargs)

    return Namespace(
        exit_code=completed.returncode,
        stdout=completed.stdout.decode(),
        stderr=completed.stderr.decode(),
    )
