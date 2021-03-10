# from ex6_mix_it.project.technology.technology import Technology
from project.technology.technology import Technology


class Laptop(Technology):
    def __init__(self,
                 memory: float,
                 memory_taken: float):

        Technology.__init__(self, memory, memory_taken)

    def install_software(self, software, software_memory):
        result, check = Technology.does_device_has_memory(self.memory,
                                                          self.memory_taken,
                                                          software_memory)

        if not check:
            return f"You don't have enough space for {software}!"

        self.memory = result
        self.memory_taken += software_memory
        return self.memory
