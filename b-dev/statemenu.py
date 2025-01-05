# State machine menu example with the ability to jump to different steps
# Based in user input they chnage the name of the function and then call it
# Since the name of the function is inside While, they use blobals.get in order to access state varialbe
# If callable is used if the function can be invoked
# No classes are used, only functions

# Main menu. Has it's own wile. Returns th user input which is then used as the name of function = menu

# Main menu
def main_menu():
    while True:
        user_input = input("Main menu: 1. Play manu 2. Reserved 3. Exit")
        if user_input == "1":
            return "play_menu"
        elif user_input == "2":
            return "reserved"
        elif user_input == "3":
            return "exit"

# Main menu
def play_menu():
    while True:
        user_input = input("--Play menu: 1. Feed 2. Play 3. Main menu")
        if user_input == "1":
            feed()
        elif user_input == "2":
            return "play"
        elif user_input == "3":
            return "main_menu"

# Feed function
def feed():
    print("The dog is fed")

# Play function
def play():
    print("You played with the dog")



def state_machine():
    # Start with Main menu
    state = "main_menu"
    # If exit, gets out of while loop and terminates
    while state != "exit":
        state_function = globals().get(state)
        if callable(state_function):
            state = state_function()
        else:
            print(f"Unknown state {state}")
            break

if __name__ == "__main__":
    state_machine()