import unittest
from project.custom_list import CustomList


class TestCustomList_Repr(unittest.TestCase):
    def setUp(self) -> None:
        self.my_custom_list = CustomList(1, 2, 3, 4)

    def test_customListRepr_shouldReturnCorrectListRepresentation(self):
        expected_output = '[1, 2, 3, 4]'
        actual_output = repr(self.my_custom_list)

        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
