import unittest

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        self.pr = PlayerRepository()

    def test_set_attr(self):
        self.assertEqual(self.pr.count, 0)
        self.assertEqual(len(self.pr.players), 0)

    def test_add_raises(self):
        p = Advanced("test")
        self.pr.add(p)
        with self.assertRaises(ValueError) as ex:
            self.pr.add(p)
        self.assertEqual(str(ex.exception), "Player test already exists!")

    def test_add(self):
        p = Advanced("test")
        self.pr.add(p)
        self.assertEqual(self.pr.count, 1)
        self.assertEqual(len(self.pr.players), 1)

    def test_remove_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pr.remove("")
        self.assertEqual(str(ex.exception), "Player cannot be an empty string!")

    def test_remove(self):
        p = Advanced("test")
        self.pr.add(p)
        self.assertEqual(self.pr.count, 1)
        self.pr.remove("test")
        self.assertEqual(self.pr.count, 0)

    def test_find(self):
        p = Advanced("test")
        self.pr.add(p)
        res = self.pr.find("test")
        self.assertEqual(res.username, "test")
