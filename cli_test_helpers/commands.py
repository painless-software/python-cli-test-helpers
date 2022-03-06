"""
Useful commands for writing tests for your CLI tool
"""

from sys import version_info

try:
    from types import SimpleNamespace as Namespace
except ImportError:  # Python < 3.3
    from argparse import Namespace

if version_info < (3, 5):  # Python 2.7
    from subprocess import PIPE, CalledProcessError, check_output
elif version_info < (3, 7):
    from subprocess import PIPE, run
else:
    from subprocess import run

__all__ = []


def shell(command, **kwargs):
    """
    A better version of ``os.system()`` that captures output and returns a
    convenient namespace object.
    """
    # pylint: disable=subprocess-run-check
    if version_info < (3, 5):  # Python 2.7
        completed = Namespace(returncode=None, stdout=b"", stderr=b"")
        try:
            completed.stdout = check_output(command, shell=True, stderr=PIPE, **kwargs)
            completed.returncode = 0
        except CalledProcessError as ex:
            completed.stdout = ex.output
            completed.returncode = ex.returncode
    elif version_info < (3, 7):
        completed = run(command, shell=True, stdout=PIPE, stderr=PIPE, **kwargs)
    else:
        completed = run(command, shell=True, capture_output=True, **kwargs)

    return Namespace(
        exit_code=completed.returncode,
        stdout=completed.stdout.decode(),
        stderr=completed.stderr.decode(),
    )
