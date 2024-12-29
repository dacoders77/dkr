class Pet():
    def __init__(self):
        self.name = "Bobik"
        self.hunger = 100
        self.happiness = 20
    def play(self, hunger: int, happiness: int):
        # Apply args
        flag = False
        self.hunger += hunger
        self.happiness += happiness

        # Run through all attributes and see if negative
        for prop in vars(self).keys():
            if type(vars(self)[prop]) != str:
                if vars(self)[prop] <= 0:
                    print("One of the props <0. The action will not execute")
                    flag = True

        # If no negative values, flag = False. No need to roll back
        if flag:
            self.hunger -= hunger
            self.happiness -= happiness

# Works good
#pet = Pet()
#pet.play(-10,-10)
#print(pet.hunger, pet.happiness)

class Pet2():
    def __init__(self):
        self.name = "Bobik"
        self.hunger = 100
        self.happiness = 20

    def play(self, hunger_change: int, happiness_change: int) -> None:
        temp_changes = {"hunger": hunger_change, "happiness": happiness_change}
        flag = False
        for key, value in temp_changes.items():
            # Get values of hunger, happiness stored in object, not hunger and values passed as method arguments
            current_value = getattr(self, key, None)
            print(f"Current val: {current_value}")
            if isinstance(current_value, (int, float)):
                if current_value + value < 0:
                    print(f"Can't perform action. '{key}' will become negative")
                    flag = True

        # Roll back if negative values (validation failed)
        if flag:
            return

        # Apply changes permanently
        for key, value in temp_changes.items():
            current_value = getattr(self, key, None)
            if isinstance(current_value, (int, float)):
                setattr(self, key, current_value + value)
        print(f"Executed successfully {vars(self)}")


pet = Pet2()
pet.play(-10,-10)
