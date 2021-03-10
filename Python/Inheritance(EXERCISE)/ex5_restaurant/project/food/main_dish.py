from ex5_restaurant.project.food.food import Food
# from project.food.food import Food


class MainDish(Food):
    def __init__(self,
                 name: str,
                 price: float,
                 grams: float):

        super().__init__(name, price, grams)


dish = MainDish("chicken", 5, 500)
print(dish.name)
print(dish.price)
print(dish.grams)
