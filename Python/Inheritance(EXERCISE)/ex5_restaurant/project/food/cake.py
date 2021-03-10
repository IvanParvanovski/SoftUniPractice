# from ex5_restaurant.project.food.dessert import Dessert
from project.food.dessert import Dessert


class Cake(Dessert):
    CAKE_GRAMS = 250
    CAKE_CALORIES = 1000
    CAKE_PRICE = 5

    def __init__(self, name: str):

        super().__init__(name, Cake.CAKE_PRICE, Cake.CAKE_GRAMS, Cake.CAKE_CALORIES)
