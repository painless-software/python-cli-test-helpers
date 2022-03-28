"""
Example command module
"""
import os


def example(envvar):
    """An example command"""
    try:
        value = os.environ[envvar]
        print(f'{envvar} = {value}')
    except KeyError:
        raise SystemExit(f'Environment value {envvar} not set.')
