from project.software.software import Software


class LightSoftware(Software):
    def __init__(self,
                 name: str,
                 capacity_consumption: int,
                 memory_consumption: int):

        type = 'Light'
        capacity_consumption = int((50 / 100 * capacity_consumption) + capacity_consumption)
        memory_consumption = int(memory_consumption - (50 / 100 * memory_consumption) )

        super().__init__(name, type, capacity_consumption, memory_consumption)
