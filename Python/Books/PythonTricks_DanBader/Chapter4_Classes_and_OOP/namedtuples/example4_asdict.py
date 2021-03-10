from collections import namedtuple

Car = namedtuple('Car', 'color mileage')
red_car = Car('red', 2871)
print(red_car._asdict())
