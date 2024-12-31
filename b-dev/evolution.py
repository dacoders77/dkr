# Create base Pet class


# Puppy: Loves to play and is always energetic but needs a lot of food and attention.
# Kitten: Curious and loves to explore, but has low energy and becomes bored quickly.
# Bunny: Shy and sleepy, but very happy when well-cared for.
# Dragon: A fantasy pet with unique needs – it loves to hoard things and its hunger and energy are unusually high.
# Turtle: Slow-moving and enjoys naps, but requires regular interaction to stay happy.

# Petting: Petting your pet boosts its happiness but slightly decreases energy. Perfect for bonding.
# Training: Teach your pet tricks! This boosts energy but decreases hunger and happiness.
# Giving a Bath: Makes the pet feel refreshed, increasing energy, but it might not like it – happiness could drop temporarily.
# Play: Engages the pet in playtime, increasing happiness but making it hungrier and more tired.
# Feed: Keep your pet full! Feeding reduces hunger but might cause it to become lazy if overdone.
# Special Action - Evolution: As the pet reaches certain milestones (such as age or special achievements),
# it will evolve into a new stage. The evolution process may unlock new attributes, actions, or even a new pet type.

# You will create a base class, Pet, with shared properties like hunger, happiness, and energy +
# Then, specific pet types such as Puppy, Kitten, or Dragon will inherit from this base class ?
# and override methods to implement their own unique behaviors. This allows for efficient code reuse and organization.

# Petting: Petting your pet boosts its happiness but slightly decreases energy. Perfect for bonding.
# Training: Teach your pet tricks! This boosts energy but decreases hunger and happiness.
# Giving a Bath: Makes the pet feel refreshed, increasing energy, but it might not like it – happiness could drop temporarily.
# Play: Engages the pet in playtime, increasing happiness but making it hungrier and more tired.
# Feed: Keep your pet full! Feeding reduces hunger but might cause it to become lazy if overdone.
# Special Action - Evolution: As the pet reaches certain milestones (such as age or special achievements),
# it will evolve into a new stage. The evolution process may unlock new attributes, actions, or even a new pet type.

class Pet:
    # Shared properties
    def __init__(self, hunger, happiness, energy):
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy

    def pet(self) -> None:
        pass

    def train(self) -> None:
        pass

    def bath(self) -> None:
        pass

    def play(self) -> None:
        pass

    def feed(self) -> None:
        pass

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
        print("puppy.Petting method is overridden")


class Kitten(Pet):
    pass

class Dragon(Pet):
    pass




pup = Puppy(1,22,9)
pup.set_value(10, 20, 30)
print(pup.get_value())

print(pup.energy)

#print(help(pup)) # Good, show structure of the object!
