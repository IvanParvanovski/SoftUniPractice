import unittest
from project.custom_list import CustomList


class TestCustomList_Count(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListCount_whenDataDoesNotExist_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            element = 10
            self.my_custom_list.count(element)

        self.assertIsNotNone(context.exception)

    def test_customListCount_whenDataExists_shouldReturnTheCountOfElementsInSequence(self):
        element = 3
        expected_count = 3

        self.my_custom_list.append(3)
        self.my_custom_list.append(3)
        actual_count = self.my_custom_list.count(element)

        self.assertEqual(expected_count, actual_count)


if __name__ == '__main__':
    unittest.main()
