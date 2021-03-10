import unittest

from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    def test_beginnerInit_whenUserNameIsValid_shouldCreateObject(self):
        pl = Beginner('Ivan')

        expected_username = 'Ivan'
        actual_username = pl.username

        expected_health = 50
        actual_health = pl.health

        self.assertEqual(expected_username, actual_username)
        self.assertEqual(expected_health, actual_health)

    def test_beginnerInit_whenUsernameIsInvalid_shouldCreateObject(self):
        with self.assertRaises(Exception) as context:
            Beginner('')

        self.assertIsNotNone(context.exception)

    def test_beginnerHealthSetter_whenHealthIsLessThanZero_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            pl = Beginner('Ivan')
            pl.health = -50

        self.assertIsNotNone(context.exception)

    def test_beginnerTakeDamage_whenDamagePointsAreMoreThanPlayerHealth_shouldDecreasePlayerHealth(self):
        pl = Beginner('Ivan')
        pl.take_damage(250)

        expected_health = 0
        actual_health = pl.health

        expected_is_dead_result = True
        actual_is_dead_result = pl.is_dead

        self.assertEqual(expected_health, actual_health)
        self.assertEqual(expected_is_dead_result, actual_is_dead_result)

    def test_beginnerTakeDamage_whenDamagePointsAreNegative_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            pl = Beginner('IVP')
            pl.take_damage(-1)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()
