import unittest
# from project.cat import Cat


class CatTests(unittest.TestCase):
    def test_catEat_shouldIncreaseCatSizeBy1(self):
        """
        Cat's size is increased after eating
        """

        # Arrange
        name = 'Kitty'
        c = Cat(name)
        expected = 1

        # Act
        c.eat()

        # Assert
        self.assertEqual(expected, c.size)

    def test_catInit_whenFed_shouldReturnTrue(self):
        """
        Cat is fed after eating
        """

        # Arrange
        name = 'Kitty'
        c = Cat(name)

        # Act
        c.eat()

        # Assert
        self.assertTrue(c.fed)

    def test_catEat_whenFed_shouldRaiseError(self):
        """
        Cat cannot eat if already fed, raises an error
        """

        # Arrange
        name = 'Kitty'
        c = Cat(name)

        # Act
        with self.assertRaises(Exception) as context:
            c.eat()
            c.eat()

        # Assertion
        self.assertIsNotNone(context.exception)

    def test_catSleep_whenNotFed_shouldRaiseError(self):
        """
        Cat cannot fall asleep if not fed, raises an error
        """

        # Arrange
        name = 'Kitty'
        c = Cat(name)

        # Act
        with self.assertRaises(Exception) as context:
            c.sleep()

        # Assertion
        self.assertIsNotNone(context.exception)

    def test_catInit_whenNotSleepy_shouldRaiseError(self):
        """
        Cat is not sleepy after sleeping
        """

        # Arrange
        name = 'Kitty'
        c = Cat(name)

        # Act
        c.eat()
        c.sleep()

        # Assertion
        self.assertFalse(c.sleepy)


if __name__ == '__main__':
    unittest.main()
