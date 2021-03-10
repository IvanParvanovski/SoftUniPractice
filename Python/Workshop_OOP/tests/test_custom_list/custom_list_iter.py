import unittest
from project.custom_list import CustomList


class TestCustomList_Iter(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListIter_whenListIterationEnds_shouldResetStartingIndex(self):
        expected_index = 0

        for _ in self.my_custom_list:
            pass

        actual_index = self.my_custom_list.iter_index
        self.assertEqual(expected_index, actual_index)


if __name__ == '__main__':
    unittest.main()
