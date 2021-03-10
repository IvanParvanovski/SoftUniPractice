import unittest
from project.custom_list import CustomList


class TestCustomList_Dictionize(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListDictionize_whenOddElementsEqualEven_shouldReturnDict(self):
        expected = {1: 2, 3: 4}
        actual = self.my_custom_list.dictionize()

        self.assertDictEqual(expected, actual)

    def test_customListDictionize_whenOddElementsDoNotEqualEven_shouldReturnDict(self):
        expected = {1: 2, 3: 4, 5: ' '}
        self.my_custom_list.append(5)
        actual = self.my_custom_list.dictionize()

        self.assertDictEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
