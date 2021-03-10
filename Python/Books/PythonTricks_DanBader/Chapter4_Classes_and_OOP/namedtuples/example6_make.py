from collections import namedtuple

Car = namedtuple('Car', 'color mileage')
my_car = Car._make(['red', 2781])
print(my_car)
