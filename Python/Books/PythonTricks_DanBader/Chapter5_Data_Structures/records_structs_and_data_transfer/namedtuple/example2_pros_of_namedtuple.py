from collections import namedtuple

Car = namedtuple('Car', 'color mileage automatic')
car1 = Car('red', 3812.4, True)

# Instances have a nice repr:
print(car1)

# Accessing fields:
print(car1.mileage)

# Fields are immutable
car1.mileage = 12
car1.windshield = 'broken'
