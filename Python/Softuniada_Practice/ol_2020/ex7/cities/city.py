from abc import ABC, abstractmethod
from collections import defaultdict
from ex7.custom_exceptions.negative_numbers import NegativeNumberError


class City(ABC):
    @abstractmethod
    def __init__(self, name: str) -> None:
        self.name = name
        self.destinations = defaultdict(int)
        self.__export = 0
        self.__trucks = 0

    @property
    def export(self):
        return sum(self.destinations.values())

    @property
    def trucks(self):
        return self.__trucks

    @trucks.setter
    def trucks(self, value: int) -> None:
        if value < 0:
            raise NegativeNumberError(f"The value can't be negative: {value}")

        self.__trucks = value

    @abstractmethod
    def increase_trucks(self, value: int) -> None:
        pass

    @abstractmethod
    def decrease_trucks(self, value: int) -> None:
        pass

    def add_destination(self, destination, value):
        self.destinations[destination] = value

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'export={self.export!r}, '
                f'trucks={self.__trucks!r})')
