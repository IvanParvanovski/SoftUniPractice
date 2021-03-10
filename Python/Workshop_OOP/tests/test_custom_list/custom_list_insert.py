import unittest
from project.custom_list import CustomList


class TestCustomList_Insert(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListInsert_whenIndexIsOutOfRange_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            index = 100
            element = 5
            self.my_custom_list.insert(index, element)

        self.assertIsNotNone(context.exception)

    def test_customListInsert_whenIndexIsValid_shouldAddNewElement(self):
        expected_list = [1, 2, 3, 4, 5]
        index = 4
        element = 5

        actual_returned_list = self.my_custom_list.insert(index, element)
        actual_list = list(self.my_custom_list)

        self.assertListEqual(expected_list, actual_returned_list)
        self.assertListEqual(expected_list, actual_list)

    def test_customListInsert_whenListIsNotInteger_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            index = '5'
            element = 10
            self.my_custom_list.insert(index, element)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()
