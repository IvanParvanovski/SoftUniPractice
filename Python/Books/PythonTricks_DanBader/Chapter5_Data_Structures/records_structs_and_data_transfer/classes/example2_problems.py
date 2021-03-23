class Car:
    def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic


car1 = Car('red', 3812.4, True)
car2 = Car('blue', 402341.0, False)

# String representation is not very useful
# (Must add a manually written __repr__ method)
print(car1)
