import unittest
# from project.worker import Worker


class WorkerTests(unittest.TestCase):
    def test_workerInit_whenCorrectNameSalaryAndEnergy_shouldBeInitialized(self):
        """
        Test if the worker is initialized with correct name, salary and energy
        """

        # Arrange
        name = "Worker name"
        salary = 123
        energy = 5

        # Act
        worker = Worker(name, salary, energy)

        # Assert
        self.assertEqual(name, worker.name)
        self.assertEqual(salary, worker.salary)
        self.assertEqual(energy, worker.energy)
        self.assertEqual(0, worker.money)

    def test_workerRest_shouldIncrementEnergy(self):
        """
        Test if the worker's energy is incremented after the rest method is called
        """

        # Arrange
        name = "Worker name"
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)

        # Act
        worker.rest()

        # Assert
        self.assertEqual(energy + 1, worker.energy)

    def test_workerWork_whenEnergyIsNegativeOr0_shouldRaiseException(self):
        """
        Test if an error is raised if the worker tries to work with negative energy or equal to 0
        """

        # Arrange
        name = "Worker name"
        salary = 123
        energy = 0
        worker = Worker(name, salary, energy)

        # Act
        with self.assertRaises(Exception) as context:
            worker.work()

        # Assert
        self.assertIsNotNone(context.exception)

    def test_workerWork_whenEnergyIsAbove0_shouldIncreaseMoneyBySalary(self):
        """
        Test if the worker's money is increased by his salary correctly after the work method is called
        """

        # Arrange
        name = "Worker name"
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)

        # Act
        worker.work()

        # Assert
        self.assertEqual(salary, worker.money)

        # Act
        worker.work()

        # Assert
        self.assertEqual(salary * 2, worker.money)

    def test_workerWork_whenEnergyIsAbove0_shouldDecreaseEnergy(self):
        """
        Test if the worker's energy is decreased after the work method is called
        """

        # Arrange
        name = "Worker name"
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)

        # Act
        worker.work()

        # Assert
        self.assertEqual(energy - 1, worker.energy)

    def test_workerGetInfo_shouldReturnCorrectString(self):
        """
        Test if the get_info method returns the proper string with correct values
        """

        # Arrange
        name = "Worker name"
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)
        expected = f"{name} has saved 0 money."

        # Act
        actual = worker.get_info()

        # Assert
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
