Other Resources
===============

Click CLI Testing
-----------------

The Click CLI framework provides a dedicated `CliRunner`_ object for testing.

.. _CliRunner: https://click.palletsprojects.com/en/latest/testing/

Project Examples
----------------

These are a few projects who use :pypi:`cli-test-helpers`. Take a look at
their tests, how they use mocks, how they structure their code to make writing
tests easy!

- :gitlab:`Coding Exercise Matrix <bittner/coding-exercise-matrix>`
- :github:`Concierge CLI <vshn/concierge-cli>`
- :github:`Kustomize Wrapper <painless-software/kustomize-wrapper>`
- :github:`PyClean <bittner/pyclean>`

Add yours via `a pull request`_, so others can learn from you!

.. _a pull request: https://github.com/painless-software/python-cli-test-helpers/pulls

GitLab CI Setup and Badges
--------------------------

If you use GitLab you can set up badges with the following generic configuration.

1. Coverage:

  - Link: ``https://gitlab.com/%{project_path}/-/graphs/%{default_branch}/charts``
  - Badge image URL: ``https://gitlab.com/%{project_path}/badges/%{default_branch}/coverage.svg``

2. Pipeline:

  - Link: ``https://gitlab.com/%{project_path}/-/pipelines``
  - Badge image URL: ``https://gitlab.com/%{project_path}/badges/%{default_branch}/pipeline.svg``

3. Releases:

  - Link: ``https://gitlab.com/%{project_path}/-/releases``
  - Badge image URL: ``https://gitlab.com/%{project_path}/-/badges/release.svg``

Package releases will be triggered by pushing a Git tag to your Git repository.
