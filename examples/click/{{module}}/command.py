"""
Example command module.
"""
import os


def example(envvar):
    """An example command."""
    try:
        value = os.environ[envvar]
        print(f'{envvar} = {value}')
    except KeyError:
        msg = f'Environment value {envvar} not set.'
        raise SystemExit(msg)
