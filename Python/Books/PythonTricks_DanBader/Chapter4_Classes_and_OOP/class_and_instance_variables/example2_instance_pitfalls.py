class Dog:
    num_legs = 4 # <--- Class bariable

    def __init__(self, name):
        self.name = name # <-- Instance variable


jack = Dog('Jack')
jill = Dog('Jill')

print(jack.num_legs)
Dog.num_legs = 6
print(jack.num_legs)
