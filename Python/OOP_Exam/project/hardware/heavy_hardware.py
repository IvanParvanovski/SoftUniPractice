from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self,
                 name: str,
                 capacity: int,
                 memory: int):

        type = 'Heavy'
        capacity *= 2
        memory = int(75 / 100 * memory)

        super().__init__(name, type, capacity, memory)
