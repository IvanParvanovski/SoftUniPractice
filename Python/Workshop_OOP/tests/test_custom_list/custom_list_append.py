import unittest
from project.custom_list import CustomList


class TestCustomList_Append(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListAppend_shouldReturnList(self):

        # Arrange
        expected = [1, 2, 3, 4, 5]

        # Act
        self.my_custom_list.append(5)

        # Assert
        actual = list(self.my_custom_list)
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
