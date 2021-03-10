import unittest
from project.custom_list import CustomList


class TestCustomList_OverBound(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListOverBound_whenListIsEmpty_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            test_list = CustomList()
            test_list.overbound()

        self.assertIsNotNone(context.exception)

    def test_customListOverBound_whenListContainsNegativeNumbers_shouldReturnBiggestValueIndex(self):
        expected_index = 1

        test_list = CustomList(-50, -1, -100)
        actual_index = test_list.overbound()

        self.assertEqual(expected_index, actual_index)

    def test_customListOverBound_whenListContainsPositiveNumbers_shouldReturnBiggestValueIndex(self):
        expected_index = 3
        actual_index = self.my_custom_list.overbound()

        self.assertEqual(expected_index, actual_index)


if __name__ == '__main__':
    unittest.main()
