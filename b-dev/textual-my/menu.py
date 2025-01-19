from cProfile import label
from os import remove

from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, Container, Horizontal, Vertical, Center
from textual.widgets import Header, Footer, Label, Rule, Button, Digits, Log, Static, Sparkline
from datetime import datetime


# Logging in separate console: https://textual.textualize.io/guide/devtools/

# Main app
class BorMenu(App):
    CSS_PATH = "bor_menu.tcss" # Css cam be included here as well

    # Render interface
    def compose(self) -> ComposeResult:
        # Containers:
        # App title
        self.static = Horizontal(Label("Virtual Pet Evolution v2.0"), classes="title-box")
        with Center():
            yield self.static

        # Menu
        with Center():
            but = MenuText(classes="menu-txt")
            but.border_subtitle = "Menu"
            yield but

        # Log
        with Center():
            log_box = LogBox(classes="log-box-container") # Box for log output
            log_box.border_subtitle = "Log"
            # log_box.visible = False # Works, but just hides it. Not removes from DOM
            remove(log_box)
            yield log_box

        # Sparkline test
        with Center():
            sparkline = Sparkline(
                [10, 20, 15, 30, 25, 20, 15],
            )
            yield Container(sparkline, classes="spark")




        # 3 Action buttons
        with Center():
            yield Horizontal(
        Button("Pet", variant="primary", id="play"),
                Label(" "),
                Button("Train", variant="primary"),
                Label(" "),
                Button("Bath", variant="primary"),
                Label(" "),
                Button("Play", variant="primary"),
                Label(" "),
                Button("Feed", variant="primary"),
                classes="button-box")

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

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "play":
            LOG.write_line(f"on start press but: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")

# Buttons group container with button event handlers
class MenuText(Center):
    # Render. Buttons container
    def compose(self) -> ComposeResult:
        yield Container(Label("1. Text \n2. Hello \n3. Getting dark", classes="menu-text")) # No align if not wrapped with Container

        # yield Horizontal(
        #             Button("Walk", variant="success", tooltip="tooltip", action="notify('notify is shown')"),
        #                  Label(" "),
        #                  Button("Play", id="play", variant="success"),
        #                  Label(" "),
        #                  classes="box") # CSS class assigned to the whole Horizontal group

        #lab = Label("We are gonna put a long text here, bro", id="dynamic_label", classes="delete") # Dynamic id added. Then used with # in query statement to access
        #lab.text = "we changed it"
        #lab.border_title = "ttl1"
        #lab.border_subtitle = "ttl2"
        #yield lab

    def on_mount(self) -> None:
        pass

        # Updating label's text dynamically. Works through .update not .text = 'new text'
        #dyn = self.query_one("#dynamic_label", Label)
        #dyn.update("Worked! Finnaly. SPent many time")

    # Popup toast notification
    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "play":
            LOG.write_line("on start press but")
            self.notify("It's an older code, sir, but it checks out.")



# Log container
class LogBox(Container):
    def compose(self) -> ComposeResult:
        log = Log(classes="log-window")
        yield log


#Run the app
if __name__ == "__main__":
    app = BorMenu()
    app.run()
