import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def test_set_attr(self):
        card = MagicCard("test")
        self.assertEqual(card.name, "test")
        self.assertEqual(card.damage_points, 5)
        self.assertEqual(card.health_points, 80)

    def test_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            card = MagicCard("")
        self.assertEqual(str(ex.exception), "Card's name cannot be an empty string.")

    def test_damage_points_raise(self):
        card = MagicCard("test")
        with self.assertRaises(ValueError) as ex:
            card.damage_points = -2
        self.assertEqual(str(ex.exception), "Card's damage points cannot be less than zero.")

    def test_health_points_raise(self):
        card = MagicCard("test")
        with self.assertRaises(ValueError) as ex:
            card.health_points = -2
        self.assertEqual(str(ex.exception), "Card's HP cannot be less than zero.")