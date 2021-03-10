from collections import namedtuple

Car = namedtuple('Car', 'color mileage')
my_car = Car('red', 2781)
print(my_car)
my_car = my_car._replace(color='blue')
print(my_car)
