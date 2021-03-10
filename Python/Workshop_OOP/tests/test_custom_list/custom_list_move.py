import unittest
from project.custom_list import CustomList


class TestCustomList_Move(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListMove_whenListContainsElements_shouldRemoveTheAmountOfFirstElementsAndAddThemToTheEnd(self):
        expected_list = [3, 4, 1, 2]

        actual_returned_list = self.my_custom_list.move(2)
        actual_list = list(self.my_custom_list)

        self.assertListEqual(expected_list, actual_returned_list)
        self.assertListEqual(expected_list, actual_list)

    def test_customListMove_whenListDoesNotContainElements_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            test_list = CustomList()

            test_list.move(2)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()
