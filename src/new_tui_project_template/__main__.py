"""Main application with improved CLI structure and features."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from dotenv import load_dotenv
from rich.console import Console

from new_tui_project_template.app import ParApp

from . import __application_binary__, __application_title__, __version__
from .config import load_config
from .logging_config import get_logger, setup_logging

# Create the main Typer app with rich help
app = typer.Typer(
    name=__application_binary__,
    help=f"{__application_title__} - A starter template for TUI applications",
    rich_markup_mode="rich",
    add_completion=False,
)
console = Console(stderr=True)
logger = get_logger(__name__)

# Load environment variables
load_dotenv()
load_dotenv(Path(f"~/.{__application_binary__}.env").expanduser())


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        console.print(f"[bold blue]{__application_title__}[/bold blue] version [bold green]{__version__}[/bold green]")
        raise typer.Exit()


@app.command()
def launch_tui(
    debug: Annotated[
        bool,
        typer.Option("--debug", help="Enable debug mode"),
    ] = False,
    config_file: Annotated[
        str | None,
        typer.Option("--config", help="Path to config file"),
    ] = None,
) -> None:
    """Start TUI"""
    try:
        # Load configuration
        config = load_config(config_file)

        # Override debug setting if provided via CLI
        if debug:
            config["debug"] = debug

        setup_logging(debug=config.get("debug", False))
        console.print("[bold blue]Starting TUI[/bold blue]")
        ParApp().run()

    except Exception as e:
        logger.error(f"TUI command failed: {e}")
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
