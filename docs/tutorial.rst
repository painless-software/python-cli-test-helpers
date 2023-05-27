Tutorial
========

Let's assume you use `pytest`_ for running your tests, which is certainly a
good idea. Your CLI program is called ``foobar``.

You have prepared a ``setup.py`` with a CLI entrypoint. For the tests you have
prepared a ``tests/`` folder (outside of ``foobar/``, because you don't want
your tests to be packaged up with your application code).

Then your directory layout looks somewhat like one of `our examples`_.

.. note::

    You can easily generate a CLI project of your own from one of the
    examples of Python CLI test helpers using `Copier`_, e.g.

    .. code-block:: console

        $ copier gh:painless-software/python-cli-test-helpers my-cli

.. _pytest: https://pytest.org/
.. _our examples:
    https://github.com/painless-software/python-cli-test-helpers/tree/main/examples
.. _Copier: https://copier.readthedocs.io/

Functional tests
----------------

Start with a simple set of functional tests:

- Is the entrypoint script installed? (tests the configuration in your setup.py)
- Can this package be run as a Python module? (i.e. without having to be installed)
- Is command XYZ available? etc. Cover your entire CLI usage here!

This is almost a stupid exercise: Run the command as a shell command
and inspect the exit code of the exiting process, e.g.

.. code-block:: python

    def test_runas_module():
        """Can this package be run as a Python module?"""
        result = shell('python -m foobar --help')
        assert result.exit_code == 0

.. code-block:: python

    def test_entrypoint():
        """Is entrypoint script installed? (setup.py)"""
        result = shell('foobar --help')
        assert result.exit_code == 0

The trick is that you run a non-destructive command, e.g. by using the usual
``--help`` option of every command. This should cover your entire CLI user
interface definition.

See more |example code (click-cli)|_.

Unit tests
----------

Then you're ready to take advantage of our helpers.

``ArgvContext``
+++++++++++++++

``ArgvContext`` allows you to mimic the use of specific CLI arguments:

.. code-block:: python

    def test_get_action():
        """Is action argument (get/set) available?"""
        with ArgvContext('foobar', 'get'):
            args = foobar.cli.parse_arguments()

        assert args.action == 'get'

If you don't have argument parsing in a dedicated function you can combine
this approach with mocking a target function, e.g.

.. code-block:: python

    @patch('foobar.command.baz')
    def test_cli_command(mock_command):
        """Is the correct code called when invoked via the CLI?"""
        with ArgvContext('foobar', 'baz'), pytest.raises(SystemExit):
            foobar.cli.main()

        assert mock_command.called

See more |example code (argparse-cli)|_.

``EnvironContext``
++++++++++++++++++

``EnvironContext`` allows you to mimic the presence (or absence) of
environment variables:

.. code-block:: python

    def test_fail_without_secret():
        """Must fail without a ``SECRET`` env variable specified"""
        message_regex = "Environment value SECRET not set."

        with EnvironContext(SECRET=None):
            with pytest.raises(SystemExit, match=message_regex):
                foobar.command.baz()
                pytest.fail("CLI doesn't abort with missing SECRET")

See more |example code (click-command)|_.


.. |example code (argparse-cli)| replace:: example code
.. |example code (click-cli)| replace:: example code
.. |example code (click-command)| replace:: example code

.. _example code (argparse-cli):
    https://github.com/painless-software/python-cli-test-helpers/blob/main/examples/argparse/tests/test_cli.py
.. _example code (click-cli):
    https://github.com/painless-software/python-cli-test-helpers/blob/main/examples/click/tests/test_cli.py
.. _example code (click-command):
    https://github.com/painless-software/python-cli-test-helpers/blob/main/examples/click/tests/test_command.py
