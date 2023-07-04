"""Test the functionality of the CLI module."""
from __future__ import annotations

from typer.testing import CliRunner

from app.cli import app

runner = CliRunner()


def test_entry_version_arg() -> None:
    """Test the entry method with version argument."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "app version" in result.stdout


def test_entry_no_arg() -> None:
    """Test the entry method with no arguments."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "OPTIONS" in result.stdout
