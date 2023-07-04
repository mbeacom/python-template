"""Define the CLI related functions and classes."""
from __future__ import annotations

from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from app import __version__

app = typer.Typer(help="This is an app")
console = Console()


def version_callback(value: bool) -> None:
    """Handle the version callback."""
    if value:
        typer.secho(f"app version: {__version__}", fg=typer.colors.BRIGHT_BLUE, bold=True)
        raise typer.Exit()


@app.command()
def main(
    version: Optional[bool] = typer.Option(
        None, "--version", callback=version_callback, is_eager=True, help="Display the current app version"
    ),
) -> None:
    """Handle the main entry logic."""
    pass


if __name__ == "__main__":  # pragma: no cover
    app(prog_name="app")
