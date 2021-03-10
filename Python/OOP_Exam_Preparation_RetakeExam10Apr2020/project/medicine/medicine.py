from abc import abstractmethod, ABC

from project.survivor import Survivor


class Medicine(ABC):
    @abstractmethod
    def __init__(self,
                 health_increase: int):

        self.health_increase = health_increase

    @staticmethod
    def __is_new_health_valid(value):
        return value >= 0

    @property
    def health_increase(self):
        return self._health_increase

    @health_increase.setter
    def health_increase(self, value):
        if not Medicine.__is_new_health_valid(value):
            raise ValueError('Health increase cannot be less than zero.')

        self._health_increase = value

    def apply(self, survivor: Survivor):
        survivor.health += self.health_increase
