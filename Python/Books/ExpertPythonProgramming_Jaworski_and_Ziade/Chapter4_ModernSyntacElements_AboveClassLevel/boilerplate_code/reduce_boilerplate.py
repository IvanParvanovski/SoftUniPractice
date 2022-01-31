from dataclasses import dataclass


@dataclass
class Vector:
    x: int
    y: int

    def __add__(self, other):
        """Add two vectors using + operator"""
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        """Subtract two vectors using - operator"""
        return Vector(
            self.x - other.x,
            self.y - other.y
        )


print(Vector(2, 3))
print(Vector(5, 3) + Vector(1, 2))
print(Vector(5, 3) - Vector(1, 2))
print(Vector(2, 2) == Vector(1, 1))
print(Vector(2, 2) == Vector(2, 2))
