from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = list()
    _software = list()

    @staticmethod
    def __find_hardware(hardware_name):
        return [hardware for hardware in System._hardware if hardware.name == hardware_name]

    @staticmethod
    def __find_software(software_name):
        return [software for software in System._software if software.name == software_name]

    @staticmethod
    def register_power_hardware(name: str,
                                capacity: int,
                                memory: int):

        ph = PowerHardware(name, capacity, memory)
        System._hardware.append(ph)

    @staticmethod
    def register_heavy_hardware(name: str,
                                capacity: int,
                                memory: int):
        hh = HeavyHardware(name, capacity, memory)
        System._hardware.append(hh)

    @staticmethod
    def register_express_software(hardware_name: str,
                                  name: str,
                                  capacity_consumption: int,
                                  memory_consumption: int):

        hardware_to_install = System.__find_hardware(hardware_name)

        if not hardware_to_install:
            return 'Hardware does not exist'

        hardware = hardware_to_install[0]

        es = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(es)
        except:
            return 'Software cannot be installed'

        System._software.append(es)

    @staticmethod
    def register_light_software(hardware_name: str,
                                name: str,
                                capacity_consumption: int,
                                memory_consumption: int):

        hardware_to_install = System.__find_hardware(hardware_name)

        if not hardware_to_install:
            return 'Hardware does not exist'

        hardware = hardware_to_install[0]

        ls = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(ls)
        except:
            return 'Software cannot be installed'

        System._software.append(ls)

    @staticmethod
    def release_software_component(hardware_name: str,
                                   software_name: str):

        hardware = System.__find_hardware(hardware_name)
        software = System.__find_software(software_name)

        if not hardware or not software:
            return 'Some of the components do not exist'

        hardware[0].uninstall(software[0])

    @staticmethod
    def analyze():
        result = 'System Analysis\n' \
                 f'Hardware Components: {len(System._hardware)}\n' \
                 f'Software Components: {len(System._software)}\n'

        used_memory = 0
        used_capacity = 0
        total_memory = 0
        total_capacity = 0

        for hardware in System._hardware:
            total_memory += hardware.memory
            total_capacity += hardware.capacity

            for software in hardware.software_components:
                used_memory += software.memory_consumption
                used_capacity += software.capacity_consumption

        result += f'Total Operational Memory: {used_memory} / {total_memory}\n' \
                  f'Total Capacity Taken: {used_capacity} / {total_capacity}'

        return result

    @staticmethod
    def system_split():
        result = ''

        for hardware in System._hardware:
            result += f'Hardware Component - {hardware.name}\n' \
                      f'Express Software Components: {sum(1 for software in hardware.software_components if type(software).__name__ == "ExpressSoftware")}\n' \
                      f'Light Software Components: {sum([1 for software in hardware.software_components if type(software).__name__ == "LightSoftware"])}\n' \
                      f'Memory Usage: {sum(software.memory_consumption for software in hardware.software_components)} / {hardware.memory}\n' \
                      f'Capacity Usage: {sum(software.capacity_consumption for software in hardware.software_components)} / {hardware.capacity}\n' \
                      f'Type: {hardware.type}\n' \
                      f'Software Components: {", ".join(software.name for software in hardware.software_components) if hardware.software_components else "None"}'

        return result
