class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'({self.color!r}, {self.mileage!r})')

        # return (f'{self.__class__.__name__}'
        #         f'({self.color}, {self.mileage!r})')


my_car = Car('red', 37821)
print(my_car)
# (in console)
# >>> my_car
# Car('red;, 37821)

