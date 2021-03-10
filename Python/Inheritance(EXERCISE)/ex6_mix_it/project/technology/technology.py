# from ex6_mix_it.project.capacity_mixin import CapacityMixin
from project.capacity_mixin import CapacityMixin


class Technology(CapacityMixin):
    def __init__(self,
                 memory: float,
                 memory_taken: float):

        self.memory = memory
        self.memory_taken = memory_taken

    @staticmethod
    def does_device_has_memory(memory, memory_taken, app_memory):
        expression = Technology.get_capacity(memory, memory_taken + app_memory)
        return expression, Technology.does_expression_return_number(expression)
