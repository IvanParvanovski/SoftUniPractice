class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def does_ingredient_exist(self, ingredient):
        return ingredient in self.ingredients

    def is_quantity_more_than_expected(self, quantity, ingredient):
        return self.ingredients[ingredient] - quantity <= 0

    def repr_ingredients_and_quantity(self):
        formated_ing_list = list()
        for ing, quantity in self.ingredients.items():
            formated_ing_list.append(f"{ing}: {quantity}")
        return formated_ing_list

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"

        if not self.does_ingredient_exist(ingredient):
            self.ingredients[ingredient] = 0

        self.ingredients[ingredient] += quantity
        self.price += ingredient_price * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"

        # if not self.does_ingredient_exist(ingredient):
        #     return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        #
        # if self.is_quantity_more_than_expected(quantity, ingredient):
        #     return f"Please check again the desired quantity of {ingredient}!"
        #
        # self.ingredients[ingredient] -= quantity
        # self.price -= ingredient_price * quantity

    def pizza_ordered(self):
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join(self.repr_ingredients_and_quantity())} and " \
               f"the price will be {self.price}lv. "
