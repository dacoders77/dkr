# Inheritance

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} {self.age} years old")

    def speak(self):
        print("I don't know what i say")


class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass


# Instance
p = Pet("Tim", 19)
p.speak()  # Inherited from parent class Pet

c = Cat("bill", 34)
c.speak()

d = Dog("Jill", 25)
d.speak()

f = Fish("Bubbles", 10)
f.speak()

# Called child classes or derived classes


