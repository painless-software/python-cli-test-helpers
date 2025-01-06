cli-test-helpers |latest-version|
=================================

|check-status| |test-status| |publish-status| |python-support| |license| |docs-status|

Useful helpers for writing tests for your Python CLI program.

Writing tests for a command line interface (CLI) application is `more difficult
than it seems at first sight`_. Especially, when you use the `argparse`_ module
or the `docopt`_ or `click`_ package, control of the application entry point is
a bit taken away from you.

But it's not all that bad. This package is here to help. The Painless Software
`CLI Copier template`_ offers some guidance on how to get started, and the
CLI test helpers allow you to deal with common cases, such as mocking CLI
arguments and environment variable values.

.. |latest-version| image:: https://img.shields.io/pypi/v/cli-test-helpers.svg
   :target: https://pypi.org/project/cli-test-helpers
   :alt: Latest version on PyPI
.. |check-status| image:: https://github.com/painless-software/python-cli-test-helpers/actions/workflows/check.yml/badge.svg
   :target: https://github.com/painless-software/python-cli-test-helpers/actions/workflows/check.yml
   :alt: Code checks status
.. |test-status| image:: https://github.com/painless-software/python-cli-test-helpers/actions/workflows/test.yml/badge.svg
   :target: https://github.com/painless-software/python-cli-test-helpers/actions/workflows/test.yml
   :alt: Test suite status
.. |publish-status| image:: https://github.com/painless-software/python-cli-test-helpers/actions/workflows/publish.yml/badge.svg
   :target: https://github.com/painless-software/python-cli-test-helpers/actions/workflows/publish.yml
   :alt: Latest release Status
.. |python-support| image:: https://img.shields.io/pypi/pyversions/cli-test-helpers.svg
   :target: https://pypi.org/project/cli-test-helpers
   :alt: Python versions
.. |license| image:: https://img.shields.io/pypi/l/cli-test-helpers.svg
   :target: https://github.com/painless-software/python-cli-test-helpers/blob/main/LICENSE
   :alt: Software license
.. |docs-status| image:: https://img.shields.io/readthedocs/python-cli-test-helpers/latest.svg
   :target: https://readthedocs.org/projects/python-cli-test-helpers/
   :alt: Documentation Status
.. _more difficult than it seems at first sight: https://stackoverflow.com/questions/13493288/
.. _argparse: https://docs.python.org/3/library/argparse.html
.. _click: https://click.palletsprojects.com/
.. _docopt: http://docopt.org/
.. _documentation: https://python-cli-test-helpers.readthedocs.io/
.. _CLI Copier template: https://gitlab.com/painless-software/cicd/app/cli
.. _CONTRIBUTING: https://github.com/painless-software/python-cli-test-helpers/blob/main/CONTRIBUTING.rst

.. links-marker

Documentation
-------------

See the `documentation`_ for installation instructions and a tutorial.

Examples / Quickstart
---------------------

Visit the Painless Software `CLI Copier template`_ to inspect hands-on CLI
application blueprints for the most popular CLI frameworks. The Copier tool
lets you create your own CLI application project with tests and modern CI/CD,
effortlessly.

Development
-----------

See `CONTRIBUTING`_.
