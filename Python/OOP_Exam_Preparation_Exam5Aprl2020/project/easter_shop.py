from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory
from collections import defaultdict


class EasterShop:
    def __init__(self,
                 name: str,
                 chocolate_factory: ChocolateFactory,
                 egg_factory: EggFactory,
                 paint_factory: PaintFactory):

        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = defaultdict(int)

    def add_chocolate_ingredient(self, type: str, quantity: int):
        self.chocolate_factory.add_ingredient(type, quantity)

    def add_egg_ingredient(self, type: str, quantity: int):
        self.egg_factory.add_ingredient(type, quantity)

    def add_paint_ingredient(self, type: str, quantity: int):
        self.paint_factory.add_ingredient(type, quantity)

    def make_chocolate(self, recipe: str):
        self.chocolate_factory.make_chocolate(recipe)
        self.storage[recipe] += 1

    def paint_egg(self, color: str, egg_type: str):

        if not self.egg_factory.does_ingredient_exist(egg_type):
            raise ValueError('Invalid commands')

        if not self.paint_factory.does_ingredient_exist(color):
            raise ValueError('Invalid commands')

        self.storage[f'{color} {egg_type}'] += 1
        self.paint_factory.remove_ingredient(color, 1)
        self.egg_factory.remove_ingredient(egg_type, 1)

    def __repr__(self):
        result = f'Shop name: {self.name}\n' \
                 f'Shop Storage:'

        for k, v in self.storage.items():
            result += f'\n{k}: {v}'

        return result
