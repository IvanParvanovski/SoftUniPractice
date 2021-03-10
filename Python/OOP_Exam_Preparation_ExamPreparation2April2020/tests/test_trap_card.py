import unittest

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def setUp(self) -> None:
        self.tc = TrapCard('Tc')

    def test_trapCardInit_shouldCreateAnObject(self):
        self.assertEqual(120, self.tc.damage_points)
        self.assertEqual(5, self.tc.health_points)

    def test_trapCardNameSetter_whenNameIsInvalid_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            TrapCard('')

        self.assertIsNotNone(context.exception)

    def test_trapCardDamagePointsSetter_whenPointsAreNegativeNumber_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            self.tc.damage_points = -5

        self.assertIsNotNone(context.exception)

    def test_trapCardHealthPointsSetter_whenPointsAreNegativeNumber_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            self.tc.health_points = -5

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()
