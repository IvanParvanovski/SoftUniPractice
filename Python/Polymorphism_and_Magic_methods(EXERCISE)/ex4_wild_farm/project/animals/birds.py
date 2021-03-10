# from ex4_wild_farm.project.animals.animal import Bird
from project.animals.animal import Bird


class Owl(Bird):
    def __init__(self,
                 name: str,
                 weight: float,
                 wing_size: float):

        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        food_weight = 0.25

        if not Bird.is_food_good(food, {"Meat"}):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += food.quantity * food_weight
        self.food_eaten += food.quantity


class Hen(Bird):
    def __init__(self,
                 name: str,
                 weight: float,
                 wing_size: float):

        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        food_weight = 0.35

        if not Bird.is_food_good(food, {"Vegetable",
                                         "Fruit",
                                         "Meat",
                                         "Seed"}):

            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += food.quantity * food_weight
        self.food_eaten += food.quantity
