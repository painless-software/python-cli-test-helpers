"""
Example command module.
"""
import os


def example(args):
    """An example command."""
    try:
        value = os.environ[args.envvar]
        print(f"{args.envvar} = {value}")
    except KeyError:
        msg = f"Environment value {args.envvar} not set."
        raise SystemExit(msg)
