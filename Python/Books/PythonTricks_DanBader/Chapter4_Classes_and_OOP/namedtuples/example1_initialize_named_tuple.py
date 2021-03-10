from collections import namedtuple

Car = namedtuple('Car', 'color mileage')


red_car = Car('red', 37281.5)
print(red_car.color)
print(red_car.mileage)
print(red_car[0])
print(red_car)
print(*red_car)
red_car.color = 'blue'
