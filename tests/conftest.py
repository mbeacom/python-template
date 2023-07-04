"""Define the pytest configuration for fixture reuse."""
import pytest
import typer


@pytest.fixture
def app():
    """Define the Typer CLI fixture."""
    return typer.Typer()
