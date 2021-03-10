from project.factory.factory import Factory
from collections import defaultdict


class ChocolateFactory(Factory):
    POSSIBLE_INGREDIENTS = ("white chocolate",
                            "dark chocolate",
                            "milk chocolate",
                            "sugar")

    def __init__(self,
                 name: str,
                 capacity: int):

        super().__init__(name, capacity)
        # {recipe_name: {ingredients}}
        self.recipes = dict()
        # {recipe_name: made_recipes}
        self.products = defaultdict(int)

    def __does_recipe_exist(self, recipe_name):
        return recipe_name in self.recipes

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if not self.can_add(quantity):
            raise ValueError('Not enough space in factory')

        if not Factory._is_ingredient_valid(ingredient=ingredient_type,
                                            collection=ChocolateFactory.POSSIBLE_INGREDIENTS):

            raise TypeError(f'Ingredient of type {ingredient_type} '
                            f'not allowed in {type(self).__name__}')

        self.ingredients[ingredient_type] += quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if not Factory._is_ingredient_valid(ingredient=ingredient_type,
                                            collection=self.ingredients):
            raise KeyError('No such product in the factory')

        if not Factory._is_quantity_enough(self, ingredient_type, quantity):
            raise ValueError('Ingredient quantity cannot be less than zero')

        self.ingredients[ingredient_type] -= quantity

    def add_recipe(self, recipe_name: str, recipe: dict):
        self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        if not ChocolateFactory.__does_recipe_exist(self, recipe_name):
            raise TypeError('No such recipe')

        used_ingredients = self.recipes[recipe_name]
        for ingredient in used_ingredients:
            ChocolateFactory.remove_ingredient(self,
                                               ingredient,
                                               used_ingredients[ingredient])

        self.products[recipe_name] += 1
