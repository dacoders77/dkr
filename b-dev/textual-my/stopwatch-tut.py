# https://textual.textualize.io/tutorial/
from cProfile import label
from time import monotonic
from textual.app import App, ComposeResult # The same for all apps
from textual.containers import HorizontalGroup, VerticalScroll
from textual.reactive import reactive
from textual.widgets import Header, Footer, Label, Rule, Button, Digits, Log


class TimeDisplay(Digits):
    # Show digits
    start_time = reactive(monotonic)
    time = reactive(0.0)
    total = reactive(0.0) # total time elapsed between clicking the start and stop buttons.

    def on_mount(self) -> None:
        # Event handlr. Call when a widget is added to the app
        self.update_timer = self.set_interval(1/60, self.update_time, pause=True)

    def update_time(self) -> None:
        # Update time to current time
        self.time = self.total + (monotonic() - self.start_time)

    def watch_time(self, time: float) -> None:
        # Called when time attribute changes
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        self.update(f"{hours:02,.0f}:{minutes:02.0f}:{seconds:05.2f}")

    def start(self) -> None:
        # Start or resume time updating
        self.start_time = monotonic()
        self.update_timer.resume()

    def stop(self) -> None:
        # Stop time updating
        self.update_timer.pause()
        self.total = monotonic() - self.start_time
        self.time = self.total

    def reset(self) -> None:
        # Reset time to zero
        self.total = 0
        self.time = 0

# My own class
class ShowText(HorizontalGroup):
    def compose(self) -> ComposeResult:
        yield Label("yo-label\n")


# Stopwatch widget
class Stopwatch(HorizontalGroup):
    # A stopwatch widget

    # Event handler on button pressed
    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        time_display = self.query_one(TimeDisplay) # get a reference to the TimeDisplay widget. How to determine which one of 3?
        if button_id == "start":
            #LOG.write_line("on start press but")
            self.notify("It's an older code, sir, but it checks out.")
            time_display.start()
            self.add_class("started") # Then these attributes are added from css
        elif button_id == "stop":
            time_display.stop()
            self.remove_class("started") # Remove att on stop click
        elif button_id == "reset":
            time_display.reset()



        # My stuff
        #show_text = self.query_one(ShowText)
        #show_text.update_label = "ff"

    def compose(self) -> ComposeResult:
        # Widgets
        yield Button("Start", id="start", variant="success") # Start id label is handled in css file
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay()

# Main app that we start
class StopwatchApp(App):
    CSS_PATH = "stopwatch03.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")] # Handle D key press. List of tuples

    # Construct the interface with widgets
    def compose(self) -> ComposeResult:
        # List of widgets to render on the screen
        yield Header()
        yield Footer()
        # Display 3 vertical elements. Activate scroll if doesn't fiit to screen. Via insertion to VerticalScroll container
        yield VerticalScroll(Stopwatch(), Stopwatch(), Stopwatch(), ShowText())
        yield Log()

        #yield Rule()
        #yield Label("yo2")  # Shows simple text

    # Output test log msg and the list of all widgets
    def on_ready(self) -> None:
        global LOG # Logging var to access from anywhere
        LOG = self.query_one(Log)
        LOG.write_line("log global good")
        #log = self.query_one(Log)
        #log.write_line("Log test yo and it works!")
        all_widgets = self.query() # Get all widgets
        #for widget in all_widgets:
        #    log.write_line(f"{widget}\n")


    # Defines actions. Methods start with _action
    def action_toggle_dark(self) -> None:
        # An action toggle to dark mode
        self.theme = ("textual-dark" if self.theme == "textual-light" else "textual-light")

if __name__ == "__main__":
    app = StopwatchApp()
    app.run()


