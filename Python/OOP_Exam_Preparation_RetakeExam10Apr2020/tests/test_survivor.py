import unittest

from project.survivor import Survivor


class TestsSurvivor(unittest.TestCase):
    def test_survivorInit_shouldCreateSurvivor(self):
        expected_name = 'Ivan'
        expected_age = 15
        expected_health = 100
        expected_needs = 100

        survivor = Survivor('Ivan', 15)
        actual_name = survivor.name
        actual_age = survivor.age
        actual_health = survivor.health
        actual_needs = survivor.needs

        self.assertEqual(expected_name, actual_name)
        self.assertEqual(expected_age, actual_age)
        self.assertEqual(expected_health, actual_health)
        self.assertEqual(expected_needs, actual_needs)

    def test_survivorNameSetter_whenNewValueIsEmptyString_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            survivor_name = ''
            survivor_age = 15

            Survivor(survivor_name, survivor_age)

        self.assertIsNotNone(context.exception)

    def test_survivorAgeSetter_whenNewValueIsNegativeNumber_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            survivor_name = 'Ivan'
            survivor_age = -15

            Survivor(survivor_name, survivor_age)

        self.assertIsNotNone(context.exception)

    def test_survivorHealthSetter_whenNewValueIsNegativeNumber_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            survivor_name = 'Ivan'
            survivor_age = 15

            sur = Survivor(survivor_name, survivor_age)
            sur.health = -10

        self.assertIsNotNone(context.exception)

    def test_survivorHealthSetter_whenNewValueIsMoreThan100_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            survivor_name = 'Ivan'
            survivor_age = 15

            sur = Survivor(survivor_name, survivor_age)
            sur.health = 101

        self.assertIsNotNone(context.exception)

    def test_survivorNeedsSetter_whenNewValueIsNegativeNumber_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            survivor_name = 'Ivan'
            survivor_age = 15

            sur = Survivor(survivor_name, survivor_age)
            sur.needs = -10

        self.assertIsNotNone(context.exception)

    def test_survivorNeedsSetter_whenNewValueIsMoreThan100_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            survivor_name = 'Ivan'
            survivor_age = 15

            sur = Survivor(survivor_name, survivor_age)
            sur.needs = 101

        self.assertIsNotNone(context.exception)

    def test_survivorNeedsSustenance_whenNeedsAreLessThan100_shouldReturnTrue(self):
        sur = Survivor('Ivan', 15)
        sur.needs = 15
        self.assertTrue(sur.needs_sustenance)

    def test_survivorNeedsSustenance_whenNeedsAre100OrMore_shouldReturnFalse(self):
        sur = Survivor('Ivan', 15)
        self.assertFalse(sur.needs_sustenance)

    def test_survivorNeedsHealing_whenHealthIsLessThan100_shouldReturnTrue(self):
        sur = Survivor('Ivan', 15)
        sur.health = 15
        self.assertTrue(sur.needs_healing)

    def test_survivorNeedsHealing_whenHealthIs100OrMore_shouldReturnFalse(self):
        sur = Survivor('Ivan', 15)
        self.assertFalse(sur.needs_healing)


if __name__ == '__main__':
    unittest.main()
