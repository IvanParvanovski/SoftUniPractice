from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self,
                 name: str,
                 capacity_consumption: int,
                 memory_consumption: int):

        type = 'Express'
        memory_consumption = 2 * memory_consumption

        super().__init__(name, type, capacity_consumption, memory_consumption)
