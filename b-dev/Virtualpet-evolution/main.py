from functions import *
import threading
from time import sleep

clear_screen()
stop_game_flag = False # Reserved for thread stop?

# Start the thread
thread = GameThread(show_main_menu)
thread.start()

# Main menu. Select Pet type
while True:
    try:
        if show_main_menu() == "continue": break
    except ValueError:
        print("Wrong input. Not a number")


# Action menu. Pet's actions
# Random events will be added here: aging, mood change etc.
while not stop_game_flag:
    try:
        show_action_menu()
    except ValueError:
        print("Wrong input. Not a number")

# Stop threads before exiting the game
thread.join()
thread.stop()
print("Game over!")