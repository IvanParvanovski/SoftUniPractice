import unittest
from project.custom_list import CustomList


class TestCustomList_Copy(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListCopy_whenShallowCopy_shouldReturnNewList(self):
        # [1, 2, 3, 4]
        expected_list = list(self.my_custom_list)
        actual_list = self.my_custom_list.copy()

        self.assertListEqual(expected_list, actual_list)
        self.assertNotEqual(id(expected_list), id(actual_list))

    def test_customListCopy_whenDeepCopy_shouldReturnNewList(self):
        test_list = CustomList([1, 2, 3], 4, 5)
        expected_list = list(test_list)
        actual_list = list(test_list.copy())

        self.assertListEqual(expected_list, actual_list)
        self.assertNotEqual(id(expected_list), id(actual_list))
        self.assertNotEqual(id(expected_list[0]), id(actual_list[0]))


if __name__ == '__main__':
    unittest.main()
