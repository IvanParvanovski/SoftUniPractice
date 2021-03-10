class Dog:
    num_legs = 4 # <--- Class bariable

    def __init__(self, name):
        self.name = name # <-- Instance variable


jack = Dog('Jack')
jill = Dog('Jill')
print((jack.name, jill.name))

print(jack.num_legs)
print(Dog.num_legs)

print(Dog.name)
