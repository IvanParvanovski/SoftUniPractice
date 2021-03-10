import unittest
from project.custom_list import CustomList


class TestCustomList_AddFirst(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListClear_shouldReturnEmptyList(self):
        expected_list = list()

        self.my_custom_list.clear()

        actual_list = list(self.my_custom_list)
        self.assertListEqual(expected_list, actual_list)


if __name__ == '__main__':
    unittest.main()
