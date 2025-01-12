import os
import ast
from pathlib import Path
from classes import * # Import all classes from classes.py for dynamic creation based in user input

# Functions

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_main_menu():
    # Render the main menu using classes that inherit from Pet using class_finder.py function
    # Instance variable will be always underlined as red because it's assigned dynamically
    print("---\nMain menu. Pet Evolution game. Select your pet:")
    user_input = int(input(show_child_classes("str")))

    if user_input == len(show_child_classes("list")) + 1:
        clear_screen()
        return "continue"

    try:
        # Dynamically creating an instance of the class
        class_name = show_child_classes("list")[user_input - 1]
        # A variable for class instance. Will be created manically based on what type of pet is selected
        class_instance_name = "instance"

        # If such class exist
        if class_name in globals():
            clear_screen()
            globals()[class_instance_name] = globals()[class_name](1, 2, 3)  # Create instance
            print(f"You selected the Pet: {instance.__class__.__name__}")
        else:
            print(f"Class {class_name} not found")

    except Exception as e:
        print(f"Main menu error. Index out of range. No such menu item: {e}")


def show_action_menu():
    print("---\nAction menu: \n1. Pet (petting) \n2. Train\n3. Bath\n4. Play\n5. Feed")
    # 6. Special Action - Evolution: As the pet reaches certain milestones (such as age or special achievements),
    # it will evolve into a new stage. The evolution process may unlock new attributes, actions, or even a new pet type.
    # - will be involed automatically, not by the user
    user_input = input("Enter your action: ")
    clear_screen()
    print(f"You selected the Action: {user_input}")

    try:
        pass
    except Exception as e:
        print(f"Action menu error. Index out of range. No such menu item: {e}")



# Runs through all the files in the project and find classes that inherit from Pet clas
# Then these values are used for user menu render
def find_inherited_classes(base_class = "Pet") -> list:
    path = Path(__file__).resolve().parent
    inherited_classes = []
    # Go through file structure. Get files for each dir
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    tree = ast.parse(f.read(), filename=file_path) # Get python code structure tree
                    for node in ast.walk(tree):
                        if isinstance(node, ast.ClassDef): # Find Class in the tree
                            for base in node.bases:
                                if isinstance(base, ast.Name) and base.id == base_class: # If class found inherits from Pet
                                    inherited_classes.append((node.name, file_path)) # Tuple

    if len(inherited_classes) == 0: print("Error: No classes that inherit from Pet calls found")
    return inherited_classes

# Find all classes that inherit from Pet. They wil be used as menu items
# Return as a text menu, where each class represents a pet
# Or as list for making a decision what pet type was selected by the user
def show_child_classes(like: str) -> str | list:
    # Initialize the list to hold class names
    child_classes_names = []
    pets_menu = ""  # Contains pets list as vertical menu
    menu_item_number = 1  # Menu starting number

    # Iterate through the objects returned by find_inherited_classes and make a numbered textual-exmpl menu
    for class_name, path in find_inherited_classes():
        # Append each class name to the list
        child_classes_names.append(class_name)
        # Make a text where the names will be located on separate lines
        pets_menu += str(menu_item_number) + ". " + class_name + "\n"
        menu_item_number += 1

    # Add Continue menu option at the end
    pets_menu += f"{menu_item_number}. Continue\n"

    # return child_classes_names
    if like == "str":
        return pets_menu # As str
    else:
        return child_classes_names # As list