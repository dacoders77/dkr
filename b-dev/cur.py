import curses
import threading
from time import sleep
import signal
import sys
from datetime import datetime
import time

# Handle ctrl+c
def signal_handler(sig, frame):
    print("Exiting on ctrl-c")
    sys.exit(0)

# Continuously update time
def update_time(screen, stop_event):
    while not stop_event.is_set():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        screen.addstr(0,0,f"Current time: {current_time}")
        screen.refresh()
        sleep(1)

# Handle user import from a different thread
def main(stdscr):
    signal.signal(signal.SIGINT, signal_handler) # Handle ctrl-c
    curses.curs_set(1) # Make cursor visible
    stdscr.clear()

    stop_event = threading.Event() # Event-flag to stop the thread
    thread = threading.Thread(target=update_time, args=(stdscr, stop_event)) # Start thread and call func
    thread.start()

    try:
        stdscr.addstr(2, 0, "yo?")
        stdscr.refresh()
        curses.echo() # Let user type

        user_input = ""
        row, col = 10, 0
        while True:
            char = stdscr.getch() # Get a char at a time
            if char == 10: # Press enter ascii
                break
            elif char == 27:
                break
            else:
                user_input += chr(char) # Add character to input
                stdscr.clrtoeol()
                stdscr.addstr(row, col, user_input)
                stdscr.refresh()

        stdscr.addstr(4, 4, f"Hello: {user_input}!") # Show result
        stdscr.refresh()
        time.sleep(60) # Keep the screen to see the result
    finally:
        stop_event.set() # Stop thread and cleanup
        thread.join()
        curses.curs_set(1) # Make cursor visible

if __name__ == '__main__':
    curses.wrapper(main)