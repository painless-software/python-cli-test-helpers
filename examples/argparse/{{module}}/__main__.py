"""
Helper module to run not-installed version (via ``python3 -m {{module}}``).
"""
from .cli import main

if __name__ == "__main__":
    main()  # pragma: no cover
