from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self,
                 name: str,
                 weight: float):

        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @staticmethod
    def is_food_good(food, foods: set):
        return type(food).__name__ in foods


class Bird(Animal, ABC):
    @abstractmethod
    def __init__(self, name: str,
                 weight: float,
                 wing_size: float):

        Animal.__init__(self, name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}," \
               f" {self.wing_size}," \
               f" {self.weight}," \
               f" {self.food_eaten}]"


class Mammal(Animal, ABC):
    @abstractmethod
    def __init__(self,
                 name: str,
                 weight: float,
                 living_region):

        Animal.__init__(self, name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{type(self).__name__} " \
               f"[{self.name}, " \
               f"{self.weight}, " \
               f"{self.living_region}, " \
               f"{self.food_eaten}]"
