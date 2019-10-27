cli-test-helpers |latest-version|
=================================

|build-status| |python-support| |license|

Useful helpers for writing tests for your Python CLI program.

Writing tests for a command line interface (CLI) tool may not seem strictly
straight-forward when you think in terms of unit tests. Especially, when you
use the `argparse`_ module or the `click`_ package control of the application
entry point is a bit taken away from you.

But it's not all that bad. This package is here to help. The README gives you
some guidance on how to get started, and the helpers allow you to deal with
common cases, such as mocking CLI arguments and environment variable values.

.. |latest-version| image:: https://img.shields.io/pypi/v/cli-test-helpers.svg
   :alt: Latest version on PyPI
   :target: https://pypi.org/project/cli-test-helpers
.. |build-status| image:: https://img.shields.io/travis/painless-software/cli-test-helpers/master.svg
   :alt: Build status
   :target: https://travis-ci.org/painless-software/cli-test-helpers
.. |python-support| image:: https://img.shields.io/pypi/pyversions/cli-test-helpers.svg
   :alt: Python versions
   :target: https://pypi.org/project/cli-test-helpers
.. |license| image:: https://img.shields.io/pypi/l/cli-test-helpers.svg
   :alt: Software license
   :target: https://github.com/painless-software/cli-test-helpers/blob/master/LICENSE
.. _argparse: https://docs.python.org/3/library/argparse.html
.. _click: https://click.palletsprojects.com/

Installation
============

.. code:: console

    python3 -m pip install cli-test-helpers
