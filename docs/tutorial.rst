Tutorial
========

Let's assume you use `pytest`_ for running your tests, which is certainly a
good idea. Your CLI program is called ``foobar``.

You have prepared a ``setup.py`` with a CLI entrypoint. For the tests you have
prepared a ``tests/`` folder (outside of ``foobar/``, because you don't want
your tests to be packaged up with your application code).

Then your directory layout looks somewhat like `our example`_.

.. _pytest: https://pytest.org/
.. _our example:
    https://github.com/painless-software/python-cli-test-helpers/tree/main/examples

Functional tests
----------------

Start with a simple set of functional tests:

- Is the entrypoint script installed? (tests the configuration in your setup.py)
- Can this package be run as a Python module? (i.e. without having to be installed)
- Is command XYZ available? etc. Cover your entire CLI usage here!

This is almost a stupid exercise: Run the command as a shell command
and inspect the status code of the exiting process (see |example (test-cli)|_).

The trick is that you run a non-destructive command, e.g. by using the usual
``--help`` option of every command. This should cover your entire CLI user
interface definition.

.. |example (test-cli)| replace:: example
.. _example (test-cli):
    https://github.com/painless-software/python-cli-test-helpers/blob/main/examples/tests/test_cli.py

Unit tests
----------

Then you're ready to take advantage of our helpers.

``ArgvContext`` allows you to mimic the use of specific CLI arguments:

.. code-block:: python

    @patch('foobar.command.baz')
    def test_cli_command(mock_command):
        """Is the correct code called when invoked via the CLI?"""
        with ArgvContext('foobar', 'baz'), pytest.raises(SystemExit):
            foobar.cli.main()

        assert mock_command.called

``EnvironContext`` allows you to mimic the presence of environment values:

.. code-block:: python

    def test_fail_without_secret():
        """Must fail without a ``SECRET`` environment variable specified"""
        message_regex = "Environment value SECRET not set."

        with EnvironContext(SECRET=None):
            with pytest.raises(SystemExit, match=message_regex):
                foobar.command.baz()
                pytest.fail("CLI doesn't abort with missing SECRET")

See |example (test-command)|_.

.. |example (test-command)| replace:: example
.. _example (test-command):
    https://github.com/painless-software/python-cli-test-helpers/blob/main/examples/tests/test_command.py
