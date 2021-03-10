# Harmful
class Car:
    rev = lambda self: print('Wroom!')
    crash = lambda self: print('Boom!')


my_car = Car()
my_car.rev()
my_car.crash()
