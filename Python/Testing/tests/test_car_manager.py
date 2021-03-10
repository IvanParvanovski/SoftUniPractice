import unittest
from CarManager.car_manager import Car


class TestCar(unittest.TestCase):
    def test_carMakeSetter_whenMakeIsNone_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            make = None
            model = 'M8'
            fuel_consumption = 6.7
            fuel_capacity = 50

            car = Car(make, model, fuel_consumption, fuel_capacity)

        self.assertIsNotNone(context.exception)

    def test_carMakeSetter_whenMakeIsEmpty_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            make = ''
            model = 'M8'
            fuel_consumption = 6.7
            fuel_capacity = 50

            car = Car(make, model, fuel_consumption, fuel_capacity)

        self.assertIsNotNone(context.exception)

    def test_carMakeProperty_whenMakeIsCalled_shouldReturnMake(self):
        make = 'BMW'
        model = 'M8'
        fuel_consumption = 6.7
        fuel_capacity = 50
        car = Car(make, model, fuel_consumption, fuel_capacity)

        expected = 'BMW'
        actual = car.make

        self.assertEqual(expected, actual)

    def test_carModelSetter_whenModelIsNone_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            make = 'BMW'
            model = None
            fuel_consumption = 6.7
            fuel_capacity = 50

            car = Car(make, model, fuel_consumption, fuel_capacity)

        self.assertIsNotNone(context.exception)

    def test_carModelSetter_whenModelIsEmpty_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            make = 'BMW'
            model = ''
            fuel_consumption = 6.7
            fuel_capacity = 50

            car = Car(make, model, fuel_consumption, fuel_capacity)

        self.assertIsNotNone(context.exception)

    def test_carModelProperty_whenModelIsCalled_shouldReturnModel(self):
        make = 'BMW'
        model = 'M8'
        fuel_consumption = 6.7
        fuel_capacity = 50
        car = Car(make, model, fuel_consumption, fuel_capacity)

        expected = 'M8'
        actual = car.model

        self.assertEqual(expected, actual)

    def test_carFuelConsumptionSetter_whenFuelConsumptionIsZero_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            make = 'BMW'
            model = 'M8'
            fuel_consumption = 0
            fuel_capacity = 50

            car = Car(make, model, fuel_consumption, fuel_capacity)

        self.assertIsNotNone(context.exception)

    def test_carFuelConsumptionSetter_whenFuelConsumptionIsNegative_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            make = 'BMW'
            model = 'M8'
            fuel_consumption = -6.7
            fuel_capacity = 50

            car = Car(make, model, fuel_consumption, fuel_capacity)

        self.assertIsNotNone(context.exception)

    def test_carFuelConsumptionProperty_whenFuelConsumptionIsCalled_shouldReturnFuelConsumption(self):
        make = 'BMW'
        model = 'M8'
        fuel_consumption = 6.7
        fuel_capacity = 50
        car = Car(make, model, fuel_consumption, fuel_capacity)

        expected = 6.7
        actual = car.fuel_consumption

        self.assertEqual(expected, actual)

    def test_carFuelCapacitySetter_whenFuelCapacityIsZero_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            make = 'BMW'
            model = 'M8'
            fuel_consumption = 6.7
            fuel_capacity = 0

            car = Car(make, model, fuel_consumption, fuel_capacity)

        self.assertIsNotNone(context.exception)

    def test_carFuelCapacitySetter_whenFuelCapacityIsNegative_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            make = 'BMW'
            model = 'M8'
            fuel_consumption = 6.7
            fuel_capacity = -10

            car = Car(make, model, fuel_consumption, fuel_capacity)

        self.assertIsNotNone(context.exception)

    def test_carFuelCapacityProperty_whenFuelCapacityIsCalled_shouldReturnFuelCapacity(self):
        make = 'BMW'
        model = 'M8'
        fuel_consumption = 6.7
        fuel_capacity = 50
        car = Car(make, model, fuel_consumption, fuel_capacity)

        expected = 50
        actual = car.fuel_capacity

        self.assertEqual(expected, actual)

    def test_carFuelAmountSetter_whenFuelAmountIsNegative_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            make = 'BMW'
            model = 'M8'
            fuel_consumption = 6.7
            fuel_capacity = 50
            car = Car(make, model, fuel_consumption, fuel_capacity)

            car.fuel_amount = -7

        self.assertIsNotNone(context.exception)

    def test_carFuelAmountSetter_shouldSetNewValue(self):
        make = 'BMW'
        model = 'M8'
        fuel_consumption = 6.7
        fuel_capacity = 50
        car = Car(make, model, fuel_consumption, fuel_capacity)

        expected = 10
        car.fuel_amount = 10
        actual = car.fuel_amount

        self.assertEqual(expected, actual)

    def test_carFuelAmountProperty_whenFuelAmountIsCalled_shouldReturnFuelAmount(self):
        make = 'BMW'
        model = 'M8'
        fuel_consumption = 6.7
        fuel_capacity = 50

        car = Car(make, model, fuel_consumption, fuel_capacity)
        car.fuel_amount = 8

        expected = 8
        actual = car.fuel_amount

        self.assertEqual(expected, actual)

    def test_carRefuel_shouldIncreaseFuelAmount(self):
        make = 'BMW'
        model = 'M8'
        fuel_consumption = 6.7
        fuel_capacity = 50
        car = Car(make, model, fuel_consumption, fuel_capacity)
        fuel = 10

        car.refuel(fuel)

        expected = 10
        actual = car.fuel_amount

        self.assertEqual(expected, actual)

    def test_carRefuel_whenFuelIsMoreThanFuelCapacity(self):
        make = 'BMW'
        model = 'M8'
        fuel_consumption = 6.7
        fuel_capacity = 50
        car = Car(make, model, fuel_consumption, fuel_capacity)
        fuel = 61

        car.refuel(fuel)

        expected = 50
        actual = car.fuel_amount

        self.assertEqual(expected, actual)

    def test_carRefuel_whenFuelIsZero_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            make = 'BMW'
            model = 'M8'
            fuel_consumption = 6.7
            fuel_capacity = 50
            car = Car(make, model, fuel_consumption, fuel_capacity)

            fuel = 0
            car.refuel(fuel)

        self.assertIsNotNone(context.exception)

    def test_carRefuel_whenFuelIsNegative_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            make = 'BMW'
            model = 'M8'
            fuel_consumption = 6.7
            fuel_capacity = 50
            car = Car(make, model, fuel_consumption, fuel_capacity)

            fuel = -10
            car.refuel(fuel)

        self.assertIsNotNone(context.exception)

    def test_carDrive_whenFuelAmountIsLessThanNeeded_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            make = 'BMW'
            model = 'M8'
            fuel_consumption = 5
            fuel_capacity = 50
            car = Car(make, model, fuel_consumption, fuel_capacity)

            car.drive(10)

        self.assertIsNotNone(context.exception)

    def test_carDrive_shouldDecreaseFuelAmount(self):
        make = 'BMW'
        model = 'M8'
        fuel_consumption = 5
        fuel_capacity = 50
        car = Car(make, model, fuel_consumption, fuel_capacity)

        car.refuel(1)
        car.drive(10)

        expected = 0.5
        actual = car.fuel_amount

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
