import os
from datetime import datetime
import sys

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

        print(f"vars: {vars(self.pet)}")

        temp_changes = {"hunger": hunger_change, "happiness": happiness_change,
                        "energy": energy_change, "action": action}
        flag = False
        for key, value in temp_changes.items():
            # Get values of hunger, happiness stored in class object, not hunger and values passed as method arguments
            current_value = getattr(self.pet, key, None)
            if isinstance(current_value, (int, float)):
                if current_value + value < 0:
                    print(f"Can't perform action. '{key}' will become negative")
                    flag = True

        # Roll back if negative values (validation failed)
        if flag:
            return

        # Apply changes permanently
        for key, value in temp_changes.items():
            current_value = getattr(self.pet, key, None)
            if isinstance(current_value, (int, float)):
                setattr(self.pet, key, current_value + value)
            else:
                print(f"can't set attr: {current_value}")
        print(f"Executed successfully {vars(self.pet)}")


        # Live behaviour emulation
        # if player.pet.hunger >= 100:
        #     print("Pet died because of hunger!")
        #     sys.exit()
        #
        # if player.pet.happiness <= 30:
        #     print("Getting too sad! Entertain me!")
        #
        # if player.pet.energy <= 10:
        #     print("Too tired!")


        # match action:
        #     case "Feed":
        #         print("Action: feed")
        #         print_main_menu()
        #         self.pet.feed()
        #
        #     case "Play":
        #         print("Action: play")
        #         print_main_menu()
        #         self.pet.play()
        #
        #     case "Sleep":
        #         print("Action: sleep")
        #         print_main_menu()
        #         self.pet.sleep()
        #
        #     case "Status":
        #         print("Pet's status:")
        #         print(f"Hunger: {self.pet.hunger}")
        #         print(f"Happiness: {self.pet.happiness}")
        #         print(f"Energy: {self.pet.energy}")
        #         print_main_menu()

    class Pet:
        def __init__(self):
            # Initial pet params
            self.hunger = 30
            self.happiness = 20
            self.energy = 15

def welcome():
    clear_screen()
    print(
        f"""Virtual pet simulator {datetime.now().strftime("%H:%M:%S")}
1. Feed
2. Play
3. Sleep
4. Status
5. Main menu""")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_main_menu():
    print("5. Main menu")


# Show main menu
welcome()
player = Player()

# Handle user input
while True:
    try:
        user_input = int(input("Input: "))
        clear_screen()
        match user_input:
            case 1:
                player.interact(-5,4,3, "Feed")
            case 2:
                pass
                player.interact(5, -4, 3, "Play")
            case 3:
                pass
                 #player.interact("Sleep")
            case 4:
                pass
                #player.interact("Status")
            case 5:
                print("5. Show main menu")
                welcome()
            case _:
                print("No such menu item")

    except ValueError:
        clear_screen()
        print("Not a number")



