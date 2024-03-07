# python-template

[![Validation Workflow](https://github.com/mbeacom/python-template/actions/workflows/validate.yaml/badge.svg?branch=main&event=push)](https://github.com/mbeacom/python-template/actions/workflows/validate.yaml)
[![Pre-Commit Checks Workflow](https://github.com/mbeacom/python-template/actions/workflows/pre-commit.yaml/badge.svg?branch=main&event=push)](https://github.com/mbeacom/python-template/actions/workflows/pre-commit.yaml)
[![Coverage Status](https://codecov.io/github/mbeacom/python-template/coverage.svg?branch=main)](https://codecov.io/github/mbeacom/python-template?branch=main)
[![PyPi](https://img.shields.io/pypi/v/python-template-x)](https://pypi.org/project/python-template-x/)
[![CodeQL](https://github.com/mbeacom/python-template/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/mbeacom/python-template/actions/workflows/github-code-scanning/codeql)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/mbeacom/python-template/badge)](https://securityscorecards.dev/viewer/?uri=github.com/mbeacom/python-template)

This project is an opinionated python template.

## Usage

This project uses:

- [poetry](https://python-poetry.org/) for dependency management and packaging.
- [poethepoet](https://poethepoet.natn.io/) for task running.
- [pytest](https://docs.pytest.org/en/stable/) for testing.
- [black](https://black.readthedocs.io/en/stable/) for auto-formatting.
- [mypy](https://mypy.readthedocs.io/en/stable/) for static type checking.
- [pre-commit](https://pre-commit.com/) for git hooks.
- [ruff](https://beta.ruff.rs/docs/) for linting.
- [mkdocs](https://www.mkdocs.org/) for documentation.

Ensure you have installed the relevant dependencies before continuing.

### Install dependencies

```bash
poetry install
```

### Run tests

```bash
poetry run poe test
```

## GitHub Actions Setup

### Validation Workflow

#### CodeCov.io

The workflow is automatically setup to pass along coverage reports to CodeCov.io.
You must set the `CODECOV_TOKEN` secret in your repository settings.
Otherwise, disable the routine in the `.github/workflows/validate.yaml` file.

### Publishing Workflow

Ensure you have Discussions enabled in your repository settings,
or remove `discussion_category_name` from the `.github/workflows/publish.yaml` file.

#### PyPi

The workflow is automatically setup to publish to PyPi.
You must set the `POETRY_PYPI_TOKEN_PYPI` secret in your repository settings.
Otherwise, disable the routine in the `.github/workflows/publish.yaml` file.
