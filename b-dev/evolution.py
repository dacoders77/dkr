from clas_finder import *


class Pet:
    # Shared properties
    def __init__(self, hunger, happiness, energy):
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.pet_type = ""

    # Petting your pet boosts its happiness but slightly decreases energy. Perfect for bonding.
    def pet(self) -> None:
        pass

    # Teach your pet tricks! This boosts energy but decreases hunger and happiness
    def train(self) -> None:
        pass

    # Makes the pet feel refreshed, increasing energy, but it might not like it – happiness could drop temporarily.
    def bath(self) -> None:
        pass

    # Engages the pet in playtime, increasing happiness but making it hungrier and more tired.
    def play(self) -> None:
        pass

    # Keep your pet full! Feeding reduces hunger but might cause it to become lazy if overdone
    def feed(self) -> None:
        print("feed method of class Pet is called")

    # As the pet reaches certain milestones (such as age or special achievements), it will evolve into a new stage.
    # The evolution process may unlock new attributes, actions, or even a new pet type.
    def special_action(self) -> None:
        pass

# Class Puppy inherits from Pet
# I want to add class properties to Pet which will be private, not visible from outside
# Getter and setter should be used
# Can be done via decorators: @staticmethod, @classmethod (takes cls instead of self)

# A mixin class to add properties and getters/setters to pets
class PetBaseAttributes:
    # Good way to talk about private / protected attribute. It's convention
    # Private attributes. Accessible only via getter and setter
    _hunger = None
    _happiness = None
    _energy = None

    # Getter using decorator
    # cls - stands for class. It's a referral to Class rather than to self, which stands for and instance of the class
    # Serves the same way but more correct
    @classmethod
    def set_value(cls, hunger:int, happiness:int,energy:int) -> None:
        cls._hunger = hunger
        cls._happiness = happiness
        cls._energy = energy

    # Getter method to retrieve the private attribute
    @classmethod
    def get_value(cls) -> dict:
        return {"hunger": cls._hunger, "happiness": cls._happiness, "energy": cls._energy}

class Puppy(Pet, PetBaseAttributes):
    # No constructor needed
    def pet(self) -> None:
        print("Puppy.petting method is overridden")

class Kitten(Pet):
    def pet(self) -> None:
        print("Kitten.petting method is overridden")

class Bunny(Pet):
    def pet(self) -> None:
        print("---Bunny.petting method is overridden")

class Dragon(Pet):
    def fly(self) -> None:
        print ("Dragon.fly method. NOT overriden")

class Turtle(Pet):
    def fly(self) -> None:
        print("____Turtle.fly method. NOT overriden")

# Find all classes that inherit from Pet. They wil be used as menu items
class ChildClasses:
    # Returns the list of child class either as list or as text with \n symbols (to render menu)
    @staticmethod
    def show(like: str) -> str | list:
        # Initialize the list to hold class names
        child_classes_names = []
        pets_menu = ""  # Contains pets list as vertical menu
        menu_item_number = 1  # Menu starting number

        # Iterate through the objects returned by find_inherited_classes
        for class_name, path in find_inherited_classes():
            # Append each class name to the list
            child_classes_names.append(class_name)
            # Make a text where the names will be located on separate lines
            pets_menu += str(menu_item_number) + ". " + class_name + "\n"
            menu_item_number += 1

        # return child_classes_names
        if like == "str":
            return pets_menu
        else:
            return child_classes_names




# Functions

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_menu():
    print("Welcome to Virtual Pet Evolution game!")

def show_main_menu():
    # Render the main menu using classes that inherit from Pet using class_finder.py function
    # The menu already returned as the line items
    user_input = int(input(ChildClasses.show("str")))
    try:
        # Dynamically creating an instance of the class
        class_name = ChildClasses.show("list")[user_input - 1]
        # A variable for class instance. Will be created manically based on what type of pet is selected
        class_instance_name = "instance"

        # If such class exist
        if class_name in globals():
            globals()[class_instance_name] = globals()[class_name](1, 2, 3)  # Create instance
            print(f"You selected the Pet: {instance.__class__.__name__}")
        else:
            print(f"Class {class_name} not found")

    except Exception as e:
        print(f"Index out of range. No such menu item: {e}")
    return

def show_action_menu():
    user_input = input("--- Select an action")
    match user_input:
        case 1:
            print("oye 1")
            method_name = "feed"  # train, pet

            # Dump methods of 'instance'
            # methods = [func for func in dir(instance) if callable(getattr(instance, func)) and not func.startswith("__")]
            # print(methods)

            # If the dynamically created class has the following method
            if hasattr(instance, method_name):
                # Call method
                getattr(instance, method_name)()
            else:
                print(f"Method {method_name} doesn't exists in class: {instance.__class__.__name__}")

    return

# User input

clear_screen()
stop_game_flag = False

# Reserved for thread stop:
while not stop_game_flag:
    print("---\nMain menu. Pet Evolution game:")
    try:
        show_main_menu()
        show_action_menu()
    except ValueError:
        print("Wrong input. Not a number")



#    print(user_input)










#print(help(pup)) # Good, show structure of the object!
