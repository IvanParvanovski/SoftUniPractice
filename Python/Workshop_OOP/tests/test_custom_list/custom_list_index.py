import unittest
from project.custom_list import CustomList


class TestCustomList_Index(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListIndex_whenDataDoesNotExist_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            element = 10
            self.my_custom_list.index(element)

        self.assertIsNotNone(context.exception)

    def test_customListIndex_whenDataExists_shouldReturnElementIndex(self):
        element = 2
        expected_index = 1

        actual_index = self.my_custom_list.index(element)

        self.assertEqual(expected_index, actual_index)


if __name__ == '__main__':
    unittest.main()
