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
