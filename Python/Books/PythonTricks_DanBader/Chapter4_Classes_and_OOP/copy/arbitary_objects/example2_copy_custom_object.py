from copy import copy, deepcopy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point ({self.x!r}, {self.y!r})'


class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def __repr__(self):
        return f'Rectangle' \
               f'({self.top_left!r}, {self.bottom_right!r})'


rect = Rectangle(Point(0, 1), Point(5, 6))
shallow_rect = copy(rect)
deep_rect = deepcopy(rect)

print(rect)
print(shallow_rect)
print(deep_rect)

print(rect is shallow_rect)
print(rect is deep_rect)

rect.top_left.x = 999

print(rect)
print(shallow_rect)
print(deep_rect)
