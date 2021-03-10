import unittest
from project.custom_list import CustomList


class TestCustomList_Size(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListSize_shouldReturnLenOfList(self):
        expected = 4
        actual = self.my_custom_list.size()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
