import os
import sys
import threading
from time import sleep

# Create a stram, maybe a separate thread where the user input will
# Add some random events that could change the pet's state:
# Pet might get sick (lowering energy and happiness).
# Pet might find a toy (boosting happiness).


# Game Logic:
# Implement a game loop where the player can choose between feeding, playing, or letting the pet sleep.
# The game loop should also check if the pet is too hungry, tired, or unhappy to continue.

#Allow random events:
# Add some random events that could change the pet's state:
# Pet might get sick (lowering energy and happiness).
# Pet might find a toy (boosting happiness).
# Use the random module to trigger these events with a probability.

# Bonus Features:
# Add more features like the pet's age, where the pet gets older and its attributes change.
# Implement a pet health meter that displays the pet’s overall health. If the health reaches 0, the pet becomes "unhappy" and the game ends.

# Bonus task: pass name and pet name as kwargs


class Player:
    def __init__(self):
        self.name = "Volodimir"
        self.pet_name = "Bobic"
        self.pet = self.Pet() # New class instance

    # Interact with pet
    def interact(self, hunger_change: int, happiness_change: int,
                 energy_change: int, action: str) -> None:

        # Current pet's state
        print(f"Pet state:: {vars(self.pet)}")

        # Store in list all values that will apply to pet's state
        temp_changes = {"hunger": hunger_change, "happiness": happiness_change,
                        "energy": energy_change, "action": action}
        flag = False
        for key, value in temp_changes.items():

            # Get values of hunger, happiness, etc stored in class object, not hunger and
            # values passed as method arguments
            current_value = getattr(self.pet, key, None)
            if isinstance(current_value, (int, float)):
                if current_value + value < 0:
                    print(f"Can't perform action: '{key}' will become negative")
                    flag = True

        # Roll back if negative values (validation failed)
        if flag:
            return

        # Apply changes permanently
        for key, value in temp_changes.items():
            current_value = getattr(self.pet, key, None)
            if isinstance(current_value, (int, float)): # Use only numbers, the last value in list is "action"
                setattr(self.pet, key, current_value + value)
            else:
                pass
                # print(f"can't set attr: {current_value} type: {type(current_value)}")
        print(f"Executed successfully {vars(self.pet)}")


        # Live behaviour emulation
        if player.pet.hunger >= 100:
            print("Pet died because of hunger!")
            global stop_game
            stop_game = True # Signal the main loop to stop

        if player.pet.happiness <= 30:
            print("Getting too sad! Entertain me!")

        if player.pet.energy <= 10:
            print("Too tired!")

    def status(self) -> None:
         for key, value in vars(self.pet).items():
             print(f"{key}: {value}")


    class Pet:
        def __init__(self):
            # Initial pet params
            self.hunger = 30
            self.happiness = 20
            self.energy = 15

player = Player()

def welcome():
    clear_screen()
    print(
        f"""Pet state: {vars(player.pet)}
1. Feed
2. Play
3. Sleep
4. Status
5. Main menu""")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_main_menu():
    print("5. Main menu")


# Run thread here
class RandomAction(threading.Thread):
    # Constructor
    def __init__(self) -> None:
        # Since we are using a parent class - call the original constructor of that class
        # because it can use its own logic
        super().__init__()
        self.stop_event = threading.Event() # Start/stop thread flag (built-in parent class)

    # We override run method form the parent class
    def run(self) -> None:
        while not self.stop_event.is_set():
            # Call interact method. Hunger increases over time
            player.interact(2,0,0,"Feed")
            # Then call welcome
            welcome()
            sleep(1)

    # Stop method to stop the thread via setting the flag
    def stop(self):
        print("Stop the thread")
        self.stop_event.set()


# Show main menu
welcome()

# Start thread
random_thread = RandomAction()
random_thread.start()

stop_game = False # Thread flag

# User input handling
# When stop_game flag sets to False, while loop stops and the execution passes forward
# And there is the actual stop thread execution
while not stop_game:
    try:
        user_input = int(input("Input: "))
        clear_screen()
        match user_input:
            case 1:
                # Reduces the pet's hunger but increases its happiness and energy
                # Hunger, happiness, energy
                player.interact(-5,4,3, "Feed")
            case 2:
                # Increases the pet’s happiness, increases hunger, and decreases energy
                player.interact(8, 10, 3, "Play")
            case 3:
                # Increases energy but decreases happiness slightly.
                player.interact(0, 15, 6, "Sleep")
            case 4:
                player.status()
            case 5:
                print("5. Show main menu")
                welcome()
            case _:
                print("No such menu item")

    except ValueError:
        clear_screen()
        print("Not a number")

random_thread.stop()
random_thread.join()
print("Game over!")


