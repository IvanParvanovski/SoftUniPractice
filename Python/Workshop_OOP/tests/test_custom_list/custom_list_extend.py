import unittest
from project.custom_list import CustomList


class TestCustomList_Extend(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListExtend_whenValueIsNotIterable_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            self.my_custom_list.extend(100)

        self.assertIsNotNone(context.exception)

    def test_customListExtend_whenValueIsIterable_shouldReturnList(self):
        expected_list = [1, 2, 3, 4, 5, 6]

        actual_returned_list = self.my_custom_list.extend([5, 6])
        actual_changed_list = list(self.my_custom_list)

        self.assertListEqual(expected_list, actual_returned_list)
        self.assertListEqual(expected_list, actual_changed_list)


if __name__ == '__main__':
    unittest.main()
