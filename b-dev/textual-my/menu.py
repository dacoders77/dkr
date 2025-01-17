from cProfile import label

from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, Container, Horizontal, Vertical, Center
from textual.widgets import Header, Footer, Label, Rule, Button, Digits, Log, Static

# Logging: https://textual.textualize.io/guide/devtools/

# Main app
class BorMenu(App):
    CSS_PATH = "bor_menu.tcss" # Css cam be included here as well

    # Render interface
    def compose(self) -> ComposeResult:
        # Containers
        self.static = Horizontal(Label("Virtual Pet Evolution v2.0"), classes="box")

        with Center():
            yield self.static
        with Center():
            yield LogBox(classes="log-box")
        with Center():
            yield Buttons(classes="buttons") # Css is linked via id in render
        with Center():
            yield Horizontal(
        Button("xx", variant="primary"),
                Label(" "),
                Button("zz", variant="primary"),
                Label(" "),
                Button("cc", variant="primary"),
                classes="box")

    # Event handler. Called when a widget is added to the interface
    def on_mount(self) -> None:
        label = self.query_one(Horizontal).query_one(Label)
        label.text = "f"

        #lab = self.query_one(Label) # Get Label node from DOM
        #label.border_title = "Virtual Pet Game"
        #label.border_subtitle = "Evolution v.2"
        #self.static.styles.border = ("heavy", "yellow")
        pass

    # Output test log msg and the list of all widgets
    def on_ready(self) -> None:
        global LOG # Logging var to access from anywhere
        LOG = self.query_one(Log) # Get log widget from DOM
        LOG.write_line("log global good")

# Buttons group container with button event handlers
class Buttons(Center):
    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "play":
            LOG.write_line("on start press but")
            self.notify("It's an older code, sir, but it checks out.") # Popup toast notification

    # Render. Buttons container
    def compose(self) -> ComposeResult:
        yield Horizontal(
                    Button("Walk", variant="success", tooltip="tooltip", action="notify('notify is shown')"),
                         Label(" "),
                         Button("Play", id="play", variant="success"),
                         Label(" "),
                         classes="box") # CSS class assigned to the whole Horizontal group

# Log container
class LogBox(Container):
    def compose(self) -> ComposeResult:
        yield Log()

#Run the app
if __name__ == "__main__":
    app = BorMenu()
    app.run()
