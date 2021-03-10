import unittest

from project.card.magic_card import MagicCard
from project.card.card_repository import CardRepository


class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        self.pr = CardRepository()

    def test_set_attr(self):
        self.assertEqual(self.pr.count, 0)
        self.assertEqual(len(self.pr.cards), 0)

    def test_add_raises(self):
        p = MagicCard("test")
        self.pr.add(p)
        with self.assertRaises(ValueError) as ex:
            self.pr.add(p)
        self.assertEqual(str(ex.exception), "Card test already exists!")

    def test_add(self):
        p = MagicCard("test")
        self.pr.add(p)
        self.assertEqual(self.pr.count, 1)
        self.assertEqual(len(self.pr.cards), 1)

    def test_remove_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pr.remove("")
        self.assertEqual(str(ex.exception), "Card cannot be an empty string!")

    def test_remove(self):
        p = MagicCard("test")
        self.pr.add(p)
        self.assertEqual(self.pr.count, 1)
        self.pr.remove("test")
        self.assertEqual(self.pr.count, 0)

    def test_find(self):
        p = MagicCard("test")
        self.pr.add(p)
        res = self.pr.find("test")
        self.assertEqual(res.name, "test")
