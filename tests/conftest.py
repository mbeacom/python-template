"""Define the pytest configuration for fixture reuse."""
from __future__ import annotations

import pytest
import typer


@pytest.fixture
def app():
    """Define the Typer CLI fixture."""
    return typer.Typer()
