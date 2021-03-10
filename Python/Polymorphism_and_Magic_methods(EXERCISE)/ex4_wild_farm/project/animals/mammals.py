# from ex4_wild_farm.project.animals.animal import Mammal
from project.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self,
                 name: str,
                 weight: float,
                 living_region):

        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        food_weight = 0.10

        if not Mammal.is_food_good(food, {"Vegetable",
                                           "Fruit"}):

            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += food.quantity * food_weight
        self.food_eaten += food.quantity


class Dog(Mammal):
    def __init__(self,
                 name: str,
                 weight: float,
                 living_region):

        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        food_weight = 0.40

        if not Mammal.is_food_good(food, {"Meat"}):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += food.quantity * food_weight
        self.food_eaten += food.quantity


class Cat(Mammal):
    def __init__(self,
                 name: str,
                 weight: float,
                 living_region):

        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        food_weight = 0.30

        if not Mammal.is_food_good(food, {"Vegetable",
                                           "Meat"}):

            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += food.quantity * food_weight
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def __init__(self,
                 name: str,
                 weight: float,
                 living_region):

        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        food_weight = 1.00

        if not Mammal.is_food_good(food, {"Meat"}):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += food.quantity * food_weight
        self.food_eaten += food.quantity
