cli-test-helpers |latest-version|
=================================

|build-status| |python-support| |license|

Useful helpers for writing tests for your Python CLI program.

Writing tests for a command line interface (CLI) tool may not seem strictly
straight-forward when you think in terms of unit tests. Especially, when you
use the `argparse`_ module or the `click`_ package, control of the application
entry point is a bit taken away from you.

But it's not all that bad. This package is here to help. The examples give you
some guidance on how to get started, and the helpers allow you to deal with
common cases, such as mocking CLI arguments and environment variable values.

.. |latest-version| image:: https://img.shields.io/pypi/v/cli-test-helpers.svg
   :alt: Latest version on PyPI
   :target: https://pypi.org/project/cli-test-helpers
.. |build-status| image:: https://img.shields.io/travis/painless-software/python-cli-test-helpers/master.svg
   :alt: Build status
   :target: https://travis-ci.org/painless-software/python-cli-test-helpers
.. |python-support| image:: https://img.shields.io/pypi/pyversions/cli-test-helpers.svg
   :alt: Python versions
   :target: https://pypi.org/project/cli-test-helpers
.. |license| image:: https://img.shields.io/pypi/l/cli-test-helpers.svg
   :alt: Software license
   :target: https://github.com/painless-software/python-cli-test-helpers/blob/master/LICENSE
.. _argparse: https://docs.python.org/3/library/argparse.html
.. _click: https://click.palletsprojects.com/

Installation
============

.. code:: console

    pip install cli-test-helpers

Preferrably, though, you add `cli-test-helpers` as a dependency to your Tox
environment (see `example <examples/tox.ini#L7-L9>`__).

Usage
=====

Let's assume you use `pytest`_ for running your tests, which is certainly a
good idea. Your CLI program is called ``foobar``. You have prepared a
``setup.py`` with a CLI entrypoint. For the tests you have prepared a
``tests/`` folder (outside of ``foobar/``, because you don't want your tests
to be packaged up with your application code). Then your directory layout
looks somewhat like `our example <examples/>`__.

Functional tests
----------------

Start with a simple set of functional tests:

- Is the entrypoint script installed? (tests the configuration in your setup.py)
- Can this package be run as a Python module? (i.e. without having to be installed)
- Is command XYZ available? etc. Cover your entire CLI usage here!

This is almost a stupid exercise: Run the command as a shell command
and inspect the status code of the exiting process (see
`example <examples/tests/test_cli.py>`__). The trick is that you run a
non-destructive command, e.g. by using the usual ``--help`` option of every
command. This should cover your entire CLI user interface definition.

Unit tests
----------

Then you're ready to take advantage of our helpers.

``ArgvContext`` allows you to mimic the use of specific CLI arguments:

.. code:: python

    def test_cli_command(mock_command):
        """Is the correct code called when invoked via the CLI?"""
        with ArgvContext('foobar', 'baz'):
            foobar.command.baz()

        assert mock_command.call_count == 1

``EnvironContext`` allows you to mimic the presence of environment values:

.. code:: python

    def test_fail_without_secret():
        """Must fail without a ``SECRET`` environment variable specified"""
        message = "Environment value SECRET not set."

        with EnvironContext(SECRET=None):
            with pytest.raises(SystemExit, match=message):
                foobar.command.baz()
                pytest.fail("CLI doesn't abort with missing SECRET")

See `example <examples/tests/test_command.py>`__.

TDD
---

Remember to stick to the test-driven mantra:

#. Write one line of test code. Make the test fail.
#. Write one line of application code. Make the test pass.
#. Goto 1.


.. _pytest: https://pytest.org/
