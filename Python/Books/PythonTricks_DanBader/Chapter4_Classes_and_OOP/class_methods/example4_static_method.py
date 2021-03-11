import math


class Pizza:
    # @property
    # def radius(self):
    #     return self._radius
    #
    # @radius.setter
    # def radius(self, value):
    #     assert -360 <= value <= 360, 'Invalid Radius of the pizza! It should be less than 360 Degrees.'
    #     self._radius = value

    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    @staticmethod
    def circle_area(radius):
        return math.pow(radius, 2) * math.pi

    def area(self):
        return self.circle_area(self.radius)

    def __repr__(self):
        return (
            f'Pizza {self.radius!r} '
            f'{self.ingredients!r} '
        )

    # def __str__(self):
    #     return f'Pizza with ({", ".join(self.ingredients)})'


my_pizza = Pizza(4, ['mozarela', 'sausage'])
print(my_pizza.area())
