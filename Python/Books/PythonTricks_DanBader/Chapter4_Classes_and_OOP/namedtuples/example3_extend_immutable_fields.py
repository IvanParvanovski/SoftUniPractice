from collections import namedtuple

Car = namedtuple('Car', 'color mileage')
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge', ))
ec = ElectricCar('red', 2187, 50)
print(ec)
print(ec.color)
print(ec.mileage)
print(ec.charge)

