Examples
========

#. `argparse <argparse>`__ – *using Python's standard library and TDD*
#. `click <click>`__ – *using the Click CLI library with TDD*
#. `docopt <docopt>`__ – *using the docopt-ng CLI library with TDD*

The examples in this folder are a `Copier`_ template. You can use ``copier``
to generate a working CLI project suiting your needs, interactively selecting
one of the CLI libraries above, e.g.

.. code-block:: console

    pip install copier

.. code-block:: console

    copier gh:painless-software/python-cli-test-helpers cli-example

Add the ``--vcs-ref HEAD`` option to pick all changes from the repository that
might have been added after the latest release. See the `Copier documentation`_
for further details on generating projects from templates.

.. _Copier: https://copier.readthedocs.io/
.. _Copier documentation: https://copier.readthedocs.io/en/stable/generating/
