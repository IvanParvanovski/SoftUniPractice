from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self,
                 name: str,
                 capacity: int,
                 memory: int):

        type = 'Power'
        capacity = int(25 / 100 * capacity)
        memory = int(75 / 100 * memory + memory)

        super().__init__(name, type, capacity, memory)
