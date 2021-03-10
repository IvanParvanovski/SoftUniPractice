from copy import copy, deepcopy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point ({self.x!r}, {self.y!r})'


a = Point(23, 42)

b = copy(a)
print(a)
print(b)

print()

c = deepcopy(a)
print(a)
print(c)

print()

a.x = 5
print(a)
print(b)
print(c)