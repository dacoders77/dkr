import os

# Create a stram, maybe a separate thread where the user input will
# Add some random events that could change the pet's state:
# Pet might get sick (lowering energy and happiness).
# Pet might find a toy (boosting happiness).


class Player:
    def __init__(self): # Constructor
        self.name = "Boris"
        #self.pet = "Bobik" # Pet's name
        self.pet = self.Pet()

    class Pet:
        def feed(self):
            print("Pet:feed called")

        def play(self):
            pass

        def sleep(self):
            pass


class UserInput:
    def start(self):
            user_input = input("""
Welcome to the Virtual Pet Simulator!
What would you like to do?
1. Feed
2. Play
3. Sleep
4. Check pet status
Choose an action (1-4):
""")
            try:
                inp = int(user_input)
                return inp
            except ValueError:
                print("Not a number")

p = Player()
p.pet.feed()

# User input
u = UserInput()
while True:
    match u.start():
        case 1:
            #os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
            print(f"You entered: {u.start()}")

