from abc import ABC, abstractmethod
from collections import defaultdict


class Factory(ABC):
    @abstractmethod
    def __init__(self,
                 name: str,
                 capacity: int):

        self.name = name
        self.capacity = capacity
        # {ingredient_name: quantity}
        self.ingredients = defaultdict(int)

    @staticmethod
    def _is_ingredient_valid(ingredient, collection):
        return ingredient in collection

    def _is_quantity_enough(self, ingredient_type, needed_quantity):
        return self.ingredients[ingredient_type] - needed_quantity >= 0

    @abstractmethod
    def add_ingredient(self, ingredient_type: str, quantity: int):
        pass

    @abstractmethod
    def remove_ingredient(self,  ingredient_type: str, quantity: int):
        pass

    def can_add(self, value: int):
        return self.capacity - sum(self.ingredients.values()) - value >= 0
