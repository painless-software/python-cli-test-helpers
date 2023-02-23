cli-test-helpers |latest-version|
=================================

|check-status| |test-status| |python-support| |license| |docs-status|

Useful helpers for writing tests for your Python CLI program.

Writing tests for a command line interface (CLI) tool `may not seem strictly
straight-forward`_ when you think in terms of unit tests. Especially, when you
use the `argparse`_ module or the `click`_ package, control of the application
entry point is a bit taken away from you.

But it's not all that bad. This package is here to help. The `examples`_ give
you some guidance on how to get started, and the helpers allow you to deal with
common cases, such as mocking CLI arguments and environment variable values.

.. |latest-version| image:: https://img.shields.io/pypi/v/cli-test-helpers.svg
   :target: https://pypi.org/project/cli-test-helpers
   :alt: Latest version on PyPI
.. |check-status| image:: https://github.com/painless-software/python-cli-test-helpers/actions/workflows/check.yml/badge.svg
   :target: https://github.com/painless-software/python-cli-test-helpers/actions/workflows/check.yml
   :alt: Code checks status
.. |test-status| image:: https://github.com/painless-software/python-cli-test-helpers/actions/workflows/test.yml/badge.svg
   :target: https://github.com/painless-software/python-cli-test-helpers/actions/workflows/test.yml
   :alt: Test suite status
.. |python-support| image:: https://img.shields.io/pypi/pyversions/cli-test-helpers.svg
   :target: https://pypi.org/project/cli-test-helpers
   :alt: Python versions
.. |license| image:: https://img.shields.io/pypi/l/cli-test-helpers.svg
   :target: https://github.com/painless-software/python-cli-test-helpers/blob/main/LICENSE
   :alt: Software license
.. |docs-status| image:: https://img.shields.io/readthedocs/python-cli-test-helpers/latest.svg
   :target: https://readthedocs.org/projects/python-cli-test-helpers/
   :alt: Documentation Status
.. _may not seem strictly straight-forward: https://stackoverflow.com/questions/13493288/
.. _argparse: https://docs.python.org/3/library/argparse.html
.. _click: https://click.palletsprojects.com/
.. _documentation: https://python-cli-test-helpers.readthedocs.io/
.. _examples: https://github.com/painless-software/python-cli-test-helpers/tree/main/examples

.. links-marker

Documentation
-------------

See the `documentation`_ for installation instructions and a tutorial.

Examples
--------

The `examples`_ folder contains hands-on example projects you can start to use
directly.

Development
-----------

This project uses Tox to run its test suite. Install and use it locally like
this:

.. code-block:: shell

    python3 -m pip install tox

.. code-block:: shell

    tox -lv               # list available environments
    tox -e flake8,py310   # run a few environments
    tox -e py             # run tests with default Python
    tox                   # run entire suite

The included example projects can be tested independently with their dedicated
environments, e.g.

.. code-block:: shell

    tox -e example-docopt
