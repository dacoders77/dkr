class Person:
    number_of_people = 0
    GRAVITY = 9.8 # Constant

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

    @classmethod # Decorator
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person('Tim')
p2 = Person('Jill')
print(Person.number_of_people_())

