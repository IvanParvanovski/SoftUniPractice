import unittest
from project.custom_list import CustomList


class TestCustomList_Get(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListGet_whenListDoesNotHaveElements_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            test_list = CustomList()
            index = 2
            test_list.get(index)

        self.assertIsNotNone(context.exception)

    def test_customListGet_whenIndexIsGreaterThanListLength_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            index = 100
            self.my_custom_list.get(index)

        self.assertIsNotNone(context.exception)

    def test_customListGet_whenListContainsElementsAndIndexIsValid_shouldReturnElement(self):
        expected_element = 2
        index = 1

        actual_element = self.my_custom_list.get(index)

        self.assertEqual(expected_element, actual_element)

    def test_customListGet_whenListIsNotInteger_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            index = '5'
            self.my_custom_list.get(index)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()
