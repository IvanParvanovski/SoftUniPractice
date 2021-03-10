import unittest

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self) -> None:
        self.hardware = Hardware('Test Hardware', 'Power', 10, 10)

    def test_hardwareInstall_whenCapacityIsNotEnough_shouldRaiseException(self):
        memory_consumption = 2
        capacity_consumption = 15
        sc = Software('SSD', 'Light', capacity_consumption, memory_consumption)

        with self.assertRaises(Exception) as context:
            self.hardware.install(sc)

        self.assertIsNotNone(context.exception)

    def test_hardwareInstall_whenMemoryIsNotEnough_shouldRaiseException(self):
        memory_consumption = 10
        capacity_consumption = 51
        sc = Software('SSD', 'Light', capacity_consumption, memory_consumption)

        with self.assertRaises(Exception) as context:
            self.hardware.install(sc)

        self.assertIsNotNone(context.exception)

    def test_hardwareInstallSoftware_whenDataIsValid_shouldInstallApp(self):
        memory_consumption = 1
        capacity_consumption = 1
        sc = Software('SSD', 'Light', capacity_consumption, memory_consumption)
        expected_list = [sc]

        self.hardware.install(sc)

        actual_list = self.hardware.software_components
        self.assertListEqual(expected_list, actual_list)

    def test_hardwareInstallExpressSoftware_whenDataIsValid_shouldInstallApp(self):
        memory_consumption = 1
        capacity_consumption = 1
        sc = ExpressSoftware('SSD', capacity_consumption, memory_consumption)
        expected_list = [sc]

        self.hardware.install(sc)

        actual_list = self.hardware.software_components
        self.assertListEqual(expected_list, actual_list)

    def test_hardwareInstallLightSoftware_whenDataIsValid_shouldInstallApp(self):
        memory_consumption = 1
        capacity_consumption = 1
        sc = LightSoftware('SSD', capacity_consumption, memory_consumption)
        expected_list = [sc]

        self.hardware.install(sc)

        actual_list = self.hardware.software_components
        self.assertListEqual(expected_list, actual_list)

    def test_hardwareUninstall_whenSoftwareDoesNotExist_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            self.hardware.uninstall(Software('test', 'Light', 3, 4))

        self.assertIsNotNone(context.exception)

    def test_hardwareUninstall_whenSoftwareExists_shouldRemoveSoftware(self):
        memory_consumption = 2
        capacity_consumption = 2
        sc = Software('SSD', 'Light', capacity_consumption, memory_consumption)
        expected_list = []
        self.hardware.install(sc)

        self.hardware.uninstall(sc)

        actual_list = self.hardware.software_components
        self.assertListEqual(expected_list, actual_list)

    def test_hardwareInit_shouldCreateObject(self):
        expected_name = 'Test Hardware'
        expected_types = {'Power',
                          'Heavy'}

        expected_capacity = 10
        expected_memory = 10

        actual_name = self.hardware.name
        actual_type = self.hardware.type
        actual_capacity = self.hardware.capacity
        actual_memory = self.hardware.memory

        expected_capacity_type = isinstance(expected_capacity, int)
        expected_memory_type = isinstance(expected_memory, int)

        self.assertEqual(expected_name, actual_name)
        self.assertIn(actual_type, expected_types)
        self.assertEqual(expected_capacity, actual_capacity)
        self.assertEqual(expected_memory, actual_memory)

        self.assertTrue(expected_capacity_type)
        self.assertTrue(expected_memory_type)


if __name__ == '__main__':
    unittest.main()
