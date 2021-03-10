import unittest

from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):
    def test_advancedInit_whenUserNameIsValid_shouldCreateObject(self):
        pl = Advanced('Ivan')

        expected_username = 'Ivan'
        actual_username = pl.username

        expected_health = 250
        actual_health = pl.health

        self.assertEqual(expected_username, actual_username)
        self.assertEqual(expected_health, actual_health)

    def test_advancedInit_whenUsernameIsInvalid_shouldCreateObject(self):
        with self.assertRaises(Exception) as context:
            Advanced('')

        self.assertIsNotNone(context.exception)

    def test_advancedHealthSetter_whenHealthIsLessThanZero_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            pl = Advanced('Ivan')
            pl.health = -50

        self.assertIsNotNone(context.exception)

    def test_advancedTakeDamage_whenDamagePointsAreMoreThanPlayerHealth_shouldDecreasePlayerHealth(self):
        pl = Advanced('Ivan')
        pl.take_damage(250)

        expected_health = 0
        actual_health = pl.health

        expected_is_dead_result = True
        actual_is_dead_result = pl.is_dead

        self.assertEqual(expected_health, actual_health)
        self.assertEqual(expected_is_dead_result, actual_is_dead_result)

    def test_advancedTakeDamage_whenDamagePointsAreNegative_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            pl = Advanced('IVP')
            pl.take_damage(-1)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()
