import unittest
from project.custom_list import CustomList


class TestCustomList_Sum(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListSum_whenListContainsStringDigit_shouldReturnSumOfListElements(self):
        expected = 11
        self.my_custom_list.append('5')

        actual = self.my_custom_list.sum()

        self.assertEqual(expected, actual)

    def test_customListSum_whenListContainsFloatDigits_shouldReturnSumOfListElements(self):
        expected = 12.1
        test_list = CustomList(1, 5.1, 6)

        actual_sum = test_list.sum()

        self.assertEqual(expected, actual_sum)

    def test_customListSum_whenListContainsOnlyDigits_shouldReturnSumOfListElements(self):
        expected = 10

        actual = self.my_custom_list.sum()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
