import unittest
from project.custom_list import CustomList


class TestCustomList_Pop(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListPop_shouldReturnLastElement(self):
        expected_element = 4
        actual_element = self.my_custom_list.pop()

        self.assertEqual(expected_element, actual_element)


if __name__ == '__main__':
    unittest.main()
