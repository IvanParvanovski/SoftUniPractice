class Product:
    def __init__(self,
                 name: str,
                 price: float):

        self._name = name
        self.__price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self.__price
