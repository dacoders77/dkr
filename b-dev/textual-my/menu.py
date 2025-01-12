from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, Container
from textual.widgets import Header, Footer, Label, Rule, Button, Digits, Log, Static

class BorMenu(App):
    CSS_PATH = "bor_menu.tcss"

    # Render interface
    def compose(self) -> ComposeResult:
        yield Static("One", classes="box")
        yield Static("Two", classes="box")
        yield LogBox(classes="stat-container")
        yield Static("Three", classes="box")
        yield Stat(classes="stat-container") # Css can be applied using class name "Stat"

    # Event handler. Called when a widget is added to the interface
    # Delete? Can pul log init here?
    def on_mount(self) -> None:
        #label = self.query_one(Label) # Get Label node from DOM
        #label.border_title = "Virtual Pet Game"
        #label.border_subtitle = "Evolution v.2"
        pass

    # Output test log msg and the list of all widgets
    def on_ready(self) -> None:
        global LOG # Logging var to access from anywhere
        LOG = self.query_one(Log)
        LOG.write_line("log global good")


# Matreshka test. Worked!
class Stat(Static):
    # Event handler on button pressed
    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "start":
            LOG.write_line("on start press but")
            self.notify("It's an older code, sir, but it checks out.")

    # Render
    def compose(self) -> ComposeResult:
        yield Container(
            Button("Start4", variant="success"),
            Label(" "),
            Button("Start3", id="start", variant="primary"),
            Label(" "),
            Button("Start4", id="start4", variant="success"),
            id="horizontal-layout"
        )

# Box for log
class LogBox(Static):
    def compose(self) -> ComposeResult:
        yield Container(
            Label("yo"),
            Log(),
            id="horizontal-layout"
        )

# Buttons group
class Buttons(HorizontalGroup):
    def on_button_press(self, event: Button.Pressed) -> None:
        button_id = event.button
        if button_id == "start":
            self.notify("Button pressed")

    # Each class canh have its own yield
    def compose(self) -> ComposeResult:
        yield Button("Start", id="start", variant="success")  # Start id label is handled in css file
        yield Button("Start2", id="start2", variant="success")

# Run the app
if __name__ == "__main__":
    app = BorMenu()
    app.run()
