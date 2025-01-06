Contributing
============

If you want to improve the code base, add a feature or update the
documentation please open a `pull request`_. Feel free to `open an issue`_
beforehand to discuss your plans.

.. _pull request: https://github.com/painless-software/python-cli-test-helpers/pulls
.. _open an issue: https://github.com/painless-software/python-cli-test-helpers/issues

Development
-----------

This project uses Tox to run its test suite. Install it using Pip like this:

.. code-block:: shell

    python3 -m pip install tox

Alternatively, if you use `uv`_, install Tox as a development tool like this:

.. code-block:: shell

    uv tool install tox --with tox-uv

Usage:

.. code-block:: shell

    tox list             # list available environments
    tox -e py            # run tests with local default Python
    tox -e lint,format   # run a few environments
    tox                  # run entire suite

.. _uv: https://docs.astral.sh/uv/

Documentation
-------------

Build the documentation locally and view it in your Web browser:

.. code-block:: console

    $ tox -e clean,docs
    ...
    $ cd docs/_build/html/
    $ python -m http.server
    Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

Click on the displayed link to inspect the generated documentation.
