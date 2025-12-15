API Documentation
=================

This section describes the context managers and helper functions provided
by the CLI test helpers package.

.. module:: cli_test_helpers

Context Managers
----------------

.. autoclass:: cli_test_helpers.ArgvContext

.. autoclass:: cli_test_helpers.EnvironContext

.. autoclass:: cli_test_helpers.RandomDirectoryContext

Mixins
------

.. note::

    Used internally by all context managers, not meant for direct use.

.. autoclass:: cli_test_helpers.mixins.LoggingIsolationMixin

Utilities
---------

.. autofunction:: shell
