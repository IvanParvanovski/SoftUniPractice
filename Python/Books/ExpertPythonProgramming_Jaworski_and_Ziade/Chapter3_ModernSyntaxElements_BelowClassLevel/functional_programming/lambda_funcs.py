import math


def circle_area(radius):
    return math.pi * radius ** 2


print(circle_area(42))
print(circle_area)
print(circle_area.__class__)
print(circle_area.__name__)

circle_area = lambda radius: math.pi * radius ** 2
print(circle_area(42))
print(circle_area)
print(circle_area.__class__)
print(circle_area.__name__)

