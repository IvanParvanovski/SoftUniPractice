import unittest

from List.extended_list import IntegerList


class TestIntegerList(unittest.TestCase):
    def _test_integerListInit_whenNotOnlyIntegers_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            IntegerList(1, 2, 3, 4, 5)

        self.assertIsNotNone(context.exception)

    def test_integerListInit_whenOnlyIntegers_shouldStoreThem(self):
        values = [1, 2, 3, 4, 5]
        il = IntegerList(*values)

        self.assertListEqual(values, il.get_data())

    def test_integerListAdd_whenElementIsNotInteger_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            li = IntegerList(1, 2, 3, 4, 5)
            li.add('hi')

        self.assertIsNotNone(context.exception)

    def test_integerListInit_whenElementIsInteger_shouldBeAdded(self):
        values = [*range(1, 6)]
        expected = [*range(1, 7)]
        li = IntegerList(*values)
        li.add(6)

        self.assertListEqual(expected, li.get_data())

    def test_integerListRemoveIndex_whenIndexIsInvalid_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            li = IntegerList(1, 2, 3)
            li.remove_index(5)

        self.assertIsNotNone(context.exception)

    def test_integerListRemoveIndex_whenIndexIsValid_shouldBeRemoved(self):
        li = IntegerList(1, 2, 3)
        li.remove_index(1)
        expected = [1, 3]

        self.assertListEqual(expected, li.get_data())

    def test_integerListGet_whenIndexIsInvalid_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            li = IntegerList(1, 2, 3)
            li.get(5)

        self.assertIsNotNone(context.exception)

    def test_integerListGet_whenIndexIsValid_shouldReturnElement(self):
        li = IntegerList(1, 2, 3)
        expected = 1
        actual = li.get(0)

        self.assertEqual(expected, actual)

    def test_integerListInsert_whenIndexIsInvalid_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            li = IntegerList(1, 2, 3, 4)
            element = 6
            index = 10
            li.insert(element, index)

        self.assertIsNotNone(context.exception)

    def test_integerListInsert_whenElementIsNotInt_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            li = IntegerList(1, 2, 3, 4, 5)
            index = 0
            element = 'hi'
            li.insert(index, element)

        self.assertIsNotNone(context.exception)

    def test_integerListInsert_whenIndexAndElementAreValid_shouldInsertNewElement(self):
        li = IntegerList(1, 2, 3, 4)
        index = 2
        element = 8

        li.insert(index, element)

        expected = [1, 2, 8, 3, 4]
        actual = li.get_data()
        self.assertListEqual(expected, actual)

    def test_integerListGetBiggest_whenNoElements_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            li = IntegerList()
            li.get_biggest()

        self.assertIsNotNone(context.exception)

    def test_integerListGetBiggest_whenContainElements_shouldRaiseException(self):
        li = IntegerList(1, 89, 100)

        expected = 100
        actual = li.get_biggest()

        self.assertEqual(expected, actual)

    def test_integerListGetIndex_whenNoSuchElement_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            li = IntegerList(1, 2, 3)
            li.get_index(5)

        self.assertIsNotNone(context.exception)

    def test_integerListGetIndex_whenElementExist_shouldReturnElement(self):
        li = IntegerList(1, 2, 3)
        expected = 1
        actual = li.get_index(2)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
