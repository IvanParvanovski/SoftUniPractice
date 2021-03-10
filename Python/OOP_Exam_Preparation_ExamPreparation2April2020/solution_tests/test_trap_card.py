import unittest

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def test_set_attr(self):
        card = TrapCard("test")
        self.assertEqual(card.name, "test")
        self.assertEqual(card.damage_points, 120)
        self.assertEqual(card.health_points, 5)

    def test_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            card = TrapCard("")
        self.assertEqual(str(ex.exception), "Card's name cannot be an empty string.")

    def test_damage_points_raise(self):
        card = TrapCard("test")
        with self.assertRaises(ValueError) as ex:
            card.damage_points = -2
        self.assertEqual(str(ex.exception), "Card's damage points cannot be less than zero.")

    def test_health_points_raise(self):
        card = TrapCard("test")
        with self.assertRaises(ValueError) as ex:
            card.health_points = -2
        self.assertEqual(str(ex.exception), "Card's HP cannot be less than zero.")