from textual.app import App, ComposeResult
from textual.containers import Center
from textual.widgets import Static

# https://textual.textualize.io/how-to/center-things/s
#https://textual.textualize.io/FAQ/#how-do-i-pass-arguments-to-an-app
#https://textual.textualize.io/FAQ/#why-do-some-key-combinations-never-make-it-to-my-app


class CenterApp(App):
    """How to center things."""

    CSS = """
    Screen {
        align: center middle;
    }

    .words {
        border: white;
        width: auto;
    }
    """

    def compose(self) -> ComposeResult:
        with Center():
            yield Static("How about a nice game", classes="words")
        with Center():
            yield Static("of chess?", classes="words")


if __name__ == "__main__":
    app = CenterApp()
    app.run()