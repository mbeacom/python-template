"""Define the CLI related functions and classes."""
from __future__ import annotations

import typer

from python_template import __version__

app = typer.Typer(help="This is a python template.")


def version_callback(value: bool) -> None:  # noqa: FBT001
    """Handle the version callback."""
    if value:
        typer.secho(f"python-template version: {__version__}", fg=typer.colors.BRIGHT_GREEN, bold=True)
        raise typer.Exit


@app.command()
def main(
    version: bool
    | None = typer.Option(  # noqa: B008
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Display the current python template version",
    ),
) -> None:
    """Run the main python template logic."""
    pass


if __name__ == "__main__":  # pragma: no cover
    app(prog_name="python-template")
