import unittest
from triangle import get_magic_triangle


class Tests(unittest.TestCase):
    def test_zero(self):
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        actual = get_magic_triangle(5)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
