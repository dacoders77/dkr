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
    def __init__(self, hunger, happiness, energy):
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy

    def petting(self) -> None:
        pass

    def training(self) -> None:
        pass

    def bath(self) -> None:
        pass

    def petting(play) -> None:
        pass

    def petting(feed) -> None:
        pass

    def special_action(self) -> None:
        pass

class Puppy(Pet):
    # No constructor needed. It will be used from the parent class
    hunger = None # Private attributes. Accessible only via getter and setter
    happiness = None
    _value = None
    def petting(self) -> None:
        print("puppy.Petting method is overridden")

    # Getter using decorator
    # cls - stands for class. It's a referral to Class rather than to self, which stands for and instance of the class
    # Serves the same way but more correct
    @classmethod
    def set_value(cls, value):
        cls._value = value
ex
    # Getter method to retrieve the private attribute
    @classmethod
    def get_value(cls):
        return cls._value


class Knight(Pet):
    pass

class Dragon(Pet):
    pass

# pet = Pet(5, 21, 44)
pup = Puppy(1,22,9)
pup.set_value(10)
print(pup.get_value())