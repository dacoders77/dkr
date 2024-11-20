class Dog:

    def __init__(self, name):
        self.name = name
        print("Constructor called!")

    def get_name(self):
        return self.name

    def get_age(self):
        return 99

    # We can access variables / properties set in the __init__ constructor
    def set_age(self, age):
        self.age = age



d = Dog("Lucky")
d2 = Dog("Bill")
d.set_age(99)

print(f"1st object name: {d.get_name()}. 1st object age: {d.get_age()}")