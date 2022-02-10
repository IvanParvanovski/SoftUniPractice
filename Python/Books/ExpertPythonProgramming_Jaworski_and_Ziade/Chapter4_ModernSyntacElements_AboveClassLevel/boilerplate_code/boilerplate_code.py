class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
            self.y - other.y,
        )

    def __repr__(self):
        """Return textual representation of vector"""
        return f'<Vector: x={self.x}, y={self.y}>'

    def __eq__(self, other):
        """Compare two vectors for equality"""
        return self.x == other.x and self.y == other.y


print(Vector(2, 3))
print(Vector(5, 3) + Vector(1, 2))
print(Vector(5, 3) - Vector(1, 2))
print(Vector(2, 2) == Vector(1, 1))
print(Vector(2, 2) == Vector(2, 2))
