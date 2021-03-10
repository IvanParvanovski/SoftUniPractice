import unittest

from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    def test_set_attr(self):
        advanced = Beginner("test")
        self.assertEqual(advanced.username, "test")
        self.assertEqual(advanced.health, 50)
        self.assertEqual(advanced.card_repository.__class__.__name__, "CardRepository")
        self.assertFalse(advanced.is_dead)

    def test_username_raises(self):
        with self.assertRaises(ValueError) as ex:
            advanced = Beginner("")
        self.assertEqual(str(ex.exception), "Player's username cannot be an empty string.")

    def test_health_rases(self):
        advanced = Beginner("test")
        with self.assertRaises(ValueError) as ex:
            advanced.health = -2
        self.assertEqual(str(ex.exception), "Player's health bonus cannot be less than zero.")

    def test_is_dead(self):
        advanced = Beginner("test")
        self.assertFalse(advanced.is_dead)
        advanced.health = 0
        self.assertTrue(advanced.is_dead)

    def test_take_damage(self):
        advanced = Beginner("test")
        advanced.take_damage(40)
        self.assertEqual(advanced.health, 10)

    def test_take_damage_raises(self):
        advanced = Beginner("test")
        with self.assertRaises(ValueError) as ex:
            advanced.take_damage(-50)
        self.assertEqual(str(ex.exception), "Damage points cannot be less than zero.")