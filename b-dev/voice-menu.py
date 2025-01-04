# Tree voice type menu test

def main_menu():
    print("\nMain Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")
    choice = input("Select an option (1-4): ")
    return choice


def submenu_1():
    print("\nSubmenu 1:")
    print("1. Sub-option 1")
    print("2. Sub-option 2")
    print("3. Sub-option 3")
    print("4. Sub-option 4")
    print("5. Return to Main Menu")
    choice = input("Select an option (1-5): ")
    return choice


def submenu_2():
    print("\nSubmenu 2:")
    print("1. Sub-option A")
    print("2. Sub-option B")
    print("3. Go Back")
    print("4. Return to Main Menu")
    choice = input("Select an option (1-4): ")
    return choice


def voice_menu():
    while True:
        choice = main_menu()

        if choice == "1":
            while True:
                sub_choice = submenu_1()
                if sub_choice == "5":
                    break  # Return to Main Menu
                else:
                    print(f"You selected Sub-option {sub_choice} in Submenu 1.")

        elif choice == "2":
            while True:
                sub_choice = submenu_2()
                if sub_choice == "3":
                    break  # Go Back
                elif sub_choice == "4":
                    break  # Return to Main Menu
                else:
                    print(f"You selected Sub-option {sub_choice} in Submenu 2.")

        elif choice == "3":
            print("Option 3 selected. Perform actions here.")

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid selection. Please try again.")


# Run the voice menu
voice_menu()
