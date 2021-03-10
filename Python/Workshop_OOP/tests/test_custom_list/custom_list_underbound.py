import unittest
from project.custom_list import CustomList


class TestCustomList_UnderBound(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListUnderBound_whenListIsEmpty_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            test_list = CustomList()
            test_list.underbound()

        self.assertIsNotNone(context.exception)

    def test_customListUnderBound_whenListContainsNegativeNumbers_shouldReturnSmallestValueIndex(self):
        expected_index = 2

        test_list = CustomList(-50, -1, -100)
        actual_index = test_list.underbound()

        self.assertEqual(expected_index, actual_index)

    def test_customListUnderBound_whenListContainsPositiveNumbers_shouldReturnSmallestValueIndex(self):
        expected_index = 0
        actual_index = self.my_custom_list.underbound()

        self.assertEqual(expected_index, actual_index)


if __name__ == '__main__':
    unittest.main()
