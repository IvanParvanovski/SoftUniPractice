import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.cr = CardRepository()
        self.c1 = MagicCard('TestCard')
        self.cr.add(self.c1)

    def test_cardRepositoryAdd_whenCardAlreadyExist_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            self.cr.add(self.c1)

        self.assertIsNotNone(context.exception)

    def test_cardRepositoryAdd_whenCardDoestNotExist_shouldAddIt(self):
        expected_list = [self.c1]
        actual_list = self.cr.cards

        expected_count = 1
        actual_count = self.cr.count

        self.assertListEqual(expected_list, actual_list)
        self.assertEqual(expected_count, actual_count)

    def test_cardRepositoryRemove_whenCardNameIsInvalidString_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            self.cr.remove('test')

        self.assertIsNotNone(context.exception)

    def test_cardRepositoryRemove_whenCardNameIsValid_shouldRemoveCard(self):
        self.cr.remove('TestCard')
        expected_list = []
        actual_list = self.cr.cards

        expected_count = 0
        actual_count = self.cr.count

        self.assertListEqual(expected_list, actual_list)
        self.assertEqual(expected_count, actual_count)

    def test_cardRepositoryFind_whenCardNameIsInvalid_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            self.cr.find('test')

        self.assertIsNotNone(context.exception)

    def test_cardRepositoryFind_whenCardNameIsValid_shouldRaiseException(self):
        result = self.cr.find('TestCard')
        self.assertEqual(self.c1, result)


if __name__ == '__main__':
    unittest.main()
