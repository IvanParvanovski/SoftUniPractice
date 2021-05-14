from ex7.cities.city import City
from ex7.custom_exceptions.negative_numbers import NegativeNumberError


class EndCity(City):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    @property
    def export(self):
        return self.__export

    @export.setter
    def export(self, value):
        if value < 0:
            raise NegativeNumberError(f"The value can't be negative: {value}")

        self.__export = value

    def increase_trucks(self, value: int) -> None:
        self.trucks += value

    def decrease_trucks(self, value: int) -> None:
        pass
