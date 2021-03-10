# from ex2_zoo.project.mammal import Mammal
from project.mammal import Mammal


class Bear(Mammal):
    def __init__(self, name: str):
        super().__init__(name)
