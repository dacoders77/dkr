class Dog():
    def __init__(self, name):
        print("constructor called. name: " + name)

    def cry(self):
        pass

class Speak():
    def __init__(self, name):
        print("speak")
    def jump(self):
        print("jump")

class Bark:
    def __init__(self):
        print("bark")

class Animal(Speak):
    pass

a = Animal("jack")
a.jump()

