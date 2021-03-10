import unittest

from exercises.vehicle import Vehicle, Car, Truck


class TestVehicle(unittest.TestCase):
    def test_vehicleInit_whenCreateObject_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            fuel_quantity = 10
            fuel_consumption = 20

            params = (fuel_quantity, fuel_consumption)
            v = Vehicle(*params)

        self.assertIsNotNone(context.exception)


class TestCar(unittest.TestCase):
    def setUp(self) -> None:
        fuel_quantity = 20
        fuel_consumption = 5
        params = (fuel_quantity, fuel_consumption)

        self.c = Car(*params)

    def test_carInit_shouldCreateObject(self):
        expected_fuel_quantity = 10
        expected_fuel_consumption = 5
        actual_fuel_quantity = self.c.fuel_quantity
        actual_fuel_consumption = self.c.fuel_consumption

        self.assertEqual(expected_fuel_quantity, actual_fuel_quantity)
        self.assertEqual(expected_fuel_consumption, actual_fuel_consumption)

    def test_carDrive_whenFuelQuantityIsNotEnough_shouldReturnNone(self):
        self.c.drive(40)
        self.assertEqual(20, self.c.fuel_quantity)

    def test_carDrive_whenFuelQuantityIsEnough_shouldBeDecreased(self):
        self.c.drive(2)

        expected = 8.2
        actual = self.c.fuel_quantity
        self.assertEqual(expected, actual)

    def test_carRefuel_shouldIncreaseFuelQuantity(self):
        self.c.refuel(5)

        expected = 25
        actual = self.c.fuel_quantity
        self.assertEqual(expected, actual)


class TestTruck(unittest.TestCase):
    def setUp(self) -> None:
        fuel_quantity = 50
        fuel_consumption = 5
        params = (fuel_quantity, fuel_consumption)

        self.t = Truck(*params)

    def test_truckInit_shouldCreateObject(self):
        expected_fuel_quantity = 50
        expected_fuel_consumption = 5
        actual_fuel_quantity = self.t.fuel_quantity
        actual_fuel_consumption = self.t.fuel_consumption

        self.assertEqual(expected_fuel_quantity, actual_fuel_quantity)
        self.assertEqual(expected_fuel_consumption, actual_fuel_consumption)

    def test_truckDrive_whenFuelQuantityIsNotEnough_shouldReturnNone(self):
        self.t.drive(10)
        self.assertEqual(50, self.t.fuel_quantity)

    def test_truckDrive_whenFuelQuantityIsEnough_shouldBeDecreased(self):
        self.t.drive(2)

        expected = 36.8
        actual = self.t.fuel_quantity
        self.assertEqual(expected, actual)

    def test_truckRefuel_shouldIncreaseFuelQuantity(self):
        self.t.refuel(5)

        expected = 54.75
        actual = self.t.fuel_quantity
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
