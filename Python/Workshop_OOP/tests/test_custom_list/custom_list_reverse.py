import unittest
from project.custom_list import CustomList


class TestCustomList_Reverse(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListReverse_shouldReturnReversedList(self):
        expected_list = [4, 3, 2, 1]
        actual_list = self.my_custom_list.reverse()

        self.assertListEqual(expected_list, actual_list)


if __name__ == '__main__':
    unittest.main()
