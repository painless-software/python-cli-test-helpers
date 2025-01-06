Installation
============

You can install CLI test helpers from PyPI using Pip:

.. code-block:: console

    pip install cli-test-helpers

Tox
---

If you use `Tox`_, add ``cli-test-helpers`` as a dependency to your tox
environment (see |example (tox.ini)|_), e.g.

.. code-block:: ini

    # FILE: tox.ini

    [tox]
    envlist = py3{9,10,11,12}

    [testenv]
    deps = cli-test-helpers,pytest
    commands = pytest {posargs}

You can then run your tests without having to install dependencies for
testing, yourself:

.. code-block:: console

    tox


.. _Tox: https://tox.wiki/
.. |example (tox.ini)| replace:: example
.. _example (tox.ini):
    https://gitlab.com/painless-software/cicd/app/cli/-/blob/main/frameworks/click/tox.ini#L9-18
