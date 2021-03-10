import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.pf = PaintFactory('Galaxy', 10)

    def test_paintFactoryInit_shouldCreateObject(self):
        expected_name = 'Stars'
        expected_capacity = 5

        p = PaintFactory(expected_name, expected_capacity)

        actual_name = p.name
        actual_capacity = p.capacity

        self.assertEqual(expected_name, actual_name)
        self.assertEqual(actual_capacity, actual_capacity)
        self.assertEqual(type(p).__name__, 'PaintFactory')

    def test_paintFactoryAddIngredient_whenIngredientTypeIsInvalid_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            ingredient_type = 'orange'
            quantity = 2
            self.pf.add_ingredient(ingredient_type, quantity)

        self.assertIsNotNone(context.exception)

    def test_paintFactoryAddIngredient_whenQuantityIsInvalid_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            ingredient_type = 'blue'
            quantity = 100
            self.pf.add_ingredient(ingredient_type, quantity)

        self.assertIsNotNone(context.exception)

    def test_paintFactoryAddIngredient_whenDataIsValid_shouldAddNewIngredient(self):
        ingredient_type = 'yellow'
        quantity = 10
        self.pf.add_ingredient(ingredient_type, quantity)

        expected_dict = {'yellow': 10}
        actual_dict = self.pf.products

        actual_capacity = self.pf.capacity

        self.assertDictEqual(expected_dict, actual_dict)

    def test_paintFactoryRemoveIngredient_whenIngredientDoesNotExist_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            ingredient_type = 'yellow'
            quantity = 5
            self.pf.remove_ingredient(ingredient_type, quantity)

        self.assertIsNotNone(context.exception)

    def test_paintFactoryRemoveIngredient_whenIngredientQuantityIsMoreThanExpected_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            self.pf.add_ingredient('yellow', 10)

            ingredient_type = 'yellow'
            quantity = 15
            self.pf.remove_ingredient(ingredient_type, quantity)

        self.assertIsNotNone(context.exception)

    def test_paintFactoryRemoveIngredient_whenDataIsValid_shouldRemoveIngredientQuantity(self):
        self.pf.add_ingredient('yellow', 10)

        ingredient_type = 'yellow'
        quantity = 5
        self.pf.remove_ingredient(ingredient_type, quantity)

        expected_dict = {'yellow': 5}
        actual_dict = self.pf.products

        actual_capacity = self.pf.capacity

        self.assertDictEqual(expected_dict, actual_dict)


if __name__ == '__main__':
    unittest.main()
