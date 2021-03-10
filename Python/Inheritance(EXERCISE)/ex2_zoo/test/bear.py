# from ex2_zoo.project.animal import Animal
from project.animal import Animal


class Bear(Animal):
    def __init__(self, name: str):
        super().__init__(name)
