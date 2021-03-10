from abc import ABC, abstractmethod

# S.O.L.I.D
# Single responsibility - Check
# Open for extensions / Closed for modifications - Check
# Liskov substitution - Check
# Interface segregation - Check
# Dependency inversion - Check


class Shape(ABC):
    @abstractmethod
    def cal_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def cal_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, side, h_side):
        self.side = side
        self.h_side = h_side

    def cal_area(self):
        return self.side * self.h_side / 2


class AreaCalculator:
    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        return sum([shape.cal_area() for shape in self.shapes])


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)
