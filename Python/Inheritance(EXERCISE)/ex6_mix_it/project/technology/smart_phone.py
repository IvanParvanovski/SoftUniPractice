# from ex6_mix_it.project.technology.technology import Technology
from project.technology.technology import Technology


class SmartPhone(Technology):
    def __init__(self,
                 memory: float,
                 memory_taken: float):

        Technology.__init__(self, memory, memory_taken)

    def install_apps(self, app, app_memory):
        result, check = Technology.does_device_has_memory(self.memory,
                                                          self.memory_taken,
                                                          app_memory)

        if not check:
            return f"You don't have enough space for {app}!"

        self.memory = result
        self.memory_taken += app_memory
        return self.memory
