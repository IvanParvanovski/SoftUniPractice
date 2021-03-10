# from ex5_restaurant.project.product import Product
from project.product import Product


class Beverage(Product):
    def __init__(self,
                 name: str,
                 price: float,
                 milliliters: float):

        super().__init__(name, price)
        self._milliliters = milliliters

    @property
    def milliliters(self):
        return self._milliliters
