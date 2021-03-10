import unittest
from project.custom_list import CustomList


class TestCustomList_Remove(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListRemove_whenListDoesNotHaveElements_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            test_list = CustomList()
            index = 2
            test_list.remove(index)

        self.assertIsNotNone(context.exception)

    def test_customListRemove_whenIndexIsOutOfRange_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            index = 100
            self.my_custom_list.remove(index)

        self.assertIsNotNone(context.exception)

    def test_customListRemove_whenListContainsElementsAndIndexIsValid_shouldRemoveElement(self):
        expected_list = [1, 3, 4]
        expected_element = 2
        index = 1

        actual_element = self.my_custom_list.remove(index)
        actual_list = list(self.my_custom_list)

        self.assertListEqual(expected_list, actual_list)
        self.assertEqual(expected_element, actual_element)

    def test_customListRemove_whenListIsNotInteger_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            index = '5'
            self.my_custom_list.remove(index)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()
