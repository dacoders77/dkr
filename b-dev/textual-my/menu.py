from cProfile import label

from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, Container, Horizontal, Vertical, Center
from textual.widgets import Header, Footer, Label, Rule, Button, Digits, Log, Static


class BorMenu(App):
    CSS_PATH = "bor_menu.tcss"

    # Render interface
    def compose(self) -> ComposeResult:
        # Main horizontal containers

        self.static = Horizontal(Label("Virtual Pet Evolution v2.0"), classes="box")

        with Center():
            yield self.static
        with Center():
            yield LogBox(classes="log-box")
        with Center():
            yield Buttons(classes="buttons") # Css is linked via id in render
        with Center():
            #yield Static("of chess?", classes="words")
            #yield Button("ff", variant="primary")
            #yield Button("ff", variant="primary")
            yield Horizontal(
        Button("xx", variant="primary"),
                Label(" "),
                Button("zz", variant="primary"),
                Label(" "),
                Button("cc", variant="primary"),
                classes="box")


    # Event handler. Called when a widget is added to the interface
    # Delete? Can pul log init here?
    def on_mount(self) -> None:
        #label = self.query_one(Label) # Get Label node from DOM
        #label.border_title = "Virtual Pet Game"
        #label.border_subtitle = "Evolution v.2"
        #self.static.styles.border = ("heavy", "yellow")
        pass

    # Output test log msg and the list of all widgets
    def on_ready(self) -> None:
        global LOG # Logging var to access from anywhere
        LOG = self.query_one(Log) # Get log widget from DOM
        LOG.write_line("log global good")


# Matreshka test. Worked!
class Buttons(Center):
    # Event handler on button pressed
    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "play":
            LOG.write_line("on start press but")
            self.notify("It's an older code, sir, but it checks out.") # Popup toast notification

    # Render. Buttons container
    def compose(self) -> ComposeResult:
        yield Horizontal(Button("Walk", variant="success"),
                         Label(" "),
                         Button("Play", id="play", variant="success"),
                         Label(" "),
                         classes="box")


        #yield Button("run")

        # yield Container(
        #     Button("Feed", variant="success"),
        #     Label(" "),
        #     Button("Play", id="play", variant="primary"),
        #     Label(" "),
        #     Button("Run", id="run", variant="success"),
        #     id="buttons-container"
        # )

# Box for log
class LogBox(Container):
    def compose(self) -> ComposeResult:
        #yield Vertical(Label("f"))
        yield Log()



# Run the app
if __name__ == "__main__":
    app = BorMenu()
    app.run()
