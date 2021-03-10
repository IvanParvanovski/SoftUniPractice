from project.factory.factory import Factory


class EggFactory(Factory):
    POSSIBLE_INGREDIENTS = ("chicken egg",
                            "quail egg")

    def __init__(self,
                 name: str,
                 capacity: int):

        super().__init__(name, capacity)

    def does_ingredient_exist(self, ingredient):
        return ingredient in self.ingredients

    @property
    def products(self):
        return self.ingredients

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if not self.can_add(quantity):
            raise ValueError('Not enough space in factory')

        if not Factory._is_ingredient_valid(ingredient=ingredient_type,
                                            collection=EggFactory.POSSIBLE_INGREDIENTS):

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
