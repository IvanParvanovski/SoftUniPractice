from typing import NamedTuple


class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool


# Instances have a nice repr
car1 = Car('red', 3812.4, True)
print(car1)

# Accessing fields:
print(car1.mileage)

# Type annotations are not enforced without
# a separate type cheching tool like mypy:
print(Car('red', 'NOT_A_FLOAT', 99))

# Fields are immutable
car1.mileage = 12
car1.windshield = 'broken'



