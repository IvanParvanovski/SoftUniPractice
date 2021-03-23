class Car:
    def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic


car1 = Car('red', 3812.4, True)
car2 = Car('blue', 402341.0, False)

# Get the mileage
print(car1.mileage)

# Classes are mutable
car2.mileage = 12
car2.windshield = 'broken'

