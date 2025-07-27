from rich.console import ConsoleRenderable, RichCast
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Footer, Header, RichLog

from . import __application_title__, __version__


class ParApp(App[None]):
    CSS_PATH = "app.tcss"

    def __init__(self) -> None:
        super().__init__()
        self.logview = RichLog(id="log")
        self.logview.border_title = "Log"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        self.title = __application_title__
        yield Header()
        yield Footer()
        with Horizontal(id="main"):
            with Vertical():
                yield self.logview

    def on_mount(self) -> None:
        """Called when the app is mounted."""
        self.logview.write(f"Welcome to {__application_title__} v{__version__}!")
        self.logview.write("TUI application started successfully.")

    def logit(self, msg: ConsoleRenderable | RichCast | str | object) -> None:
        """Log a message to the RichLog widget."""
        self.logview.write(msg)
