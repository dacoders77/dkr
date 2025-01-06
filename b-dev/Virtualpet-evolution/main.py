from functions import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
stop_game_flag = False # Reserved for thread stop:

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
