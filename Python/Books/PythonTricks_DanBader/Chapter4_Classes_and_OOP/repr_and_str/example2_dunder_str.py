class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'a {self.color} car'


my_car = Car('red', 37281)
print(my_car)
# (in console)
# >>> my_car
# >>> <__main__.Car object at 0x000001BE083C0FA0>
# >>> str(my_car)
# >>> a red car
