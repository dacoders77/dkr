"""
make 3 classes:
animal - inherits from fish and dog
the only constructor is predent in fish
"""

class Dog:
    def __init__(self):
        print("Animal constructor called")
    def bark(self):
        pass

class Fish:
    def swim(self):
        print("Swim from fish")

class Animal(Dog, Fish):
    def animal(self):
        pass
    def swim(self):
        print("swimm from animal")

a = Animal()
a.swim()
Fish.swim(a) # Calling swim method, which is overridden if Animal is created



