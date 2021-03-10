# from ex2_zoo.project.reptile import Reptile
from project.reptile import Reptile


class Snake(Reptile):
    def __init__(self, name: str):
        super().__init__(name)
