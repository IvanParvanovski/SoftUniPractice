import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def setUp(self) -> None:
        self.mc = MagicCard('Mg')

    def test_magicCardInit_shouldCreateAnObject(self):
        self.assertEqual(5, self.mc.damage_points)
        self.assertEqual(80, self.mc.health_points)

    def test_magicCardNameSetter_whenNameIsInvalid_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            MagicCard('')

        self.assertIsNotNone(context.exception)

    def test_magicCardDamagePointsSetter_whenPointsAreNegativeNumber_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            self.mc.damage_points = -5

        self.assertIsNotNone(context.exception)

    def test_magicCardHealthPointsSetter_whenPointsAreNegativeNumber_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            self.mc.health_points = -5

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()
