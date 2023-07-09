# python-template

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
poetry poe test
# or: poetry run poe test
```
