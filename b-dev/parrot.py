import os
# 88 Merge sorted array
# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
from test.test_ctypes.test_array_in_pointer import Value


os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.name = "Boris"
        self.pet = self.Pet("Ryzhink")

    # This method will offer the player options to feed, play, or let the pet sleep.
    def interact(self):
        while True:
            try:
                user_input = input("""
Welcome to virtual pet simulator! 
What would you like to do?
Choose an action (1-5): """)
                number = int(user_input)
                #print(f"You entered {user_input}")
                match user_input:
                    case "1":
                        self.pet.feed()
                match user_input:
                    case "2":
                        self.pet.play()
                match user_input:
                    case "3":
                        self.pet.sleep()
                match user_input:
                    case "4":
                        self.pet.status()
                match user_input:
                    case "5":
                        break


            except ValueError:
                print("not a number")



    class Pet:
        def __init__(self, name):
            self.name = name
            self.hunger = 0
            self.happiness = 0
            self.energy = 0

        # Reduces the pet's hunger but increases its happiness and energy.
        def feed(self):
            print("You feed the pet!")
            self.hunger += 30
            self.happiness += 60
            self.energy += 80

            print(f"Hunger: {self.hunger}, happiness: {self.happiness}, energy: {self.energy}")

        # Increases the pet’s happiness but decreases energy and hunger.
        def play(self):
            pass

        # Increases energy but decreases happiness slightly.
        def sleep(self):
            pass

        #  Prints the current state of the pet, including hunger, happiness, and energy
        def status(self):
            pass



player = Player()
player.interact()


