import unittest
from project.custom_list import CustomList


class TestCustomList_AddFirst(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListAddFirst_shouldAddNewElementAtTheBeginningOfTheList(self):
        expected = [5, 1, 2, 3, 4]
        self.my_custom_list.add_first(5)
        actual = list(self.my_custom_list)

        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
