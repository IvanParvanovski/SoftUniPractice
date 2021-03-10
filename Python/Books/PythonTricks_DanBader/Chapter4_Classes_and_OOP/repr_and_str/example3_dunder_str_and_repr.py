class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return '__str__ for Car'

    def __repr__(self):
        return '__repr__ for Car'


my_car = Car('red', 37281)
print(my_car)
print(str(my_car))
print('{}'.format(my_car))

# (in console)
# >>> my_car
# >>> __repr__ for Car
print(repr(my_car))
print([my_car])
