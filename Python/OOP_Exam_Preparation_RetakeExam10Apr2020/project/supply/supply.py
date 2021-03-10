from abc import ABC, abstractmethod
from project.survivor import Survivor


class Supply(ABC):
    @abstractmethod
    def __init__(self,
                 needs_increase: int):

        self.needs_increase = needs_increase

    @staticmethod
    def __are_new_needs_valid(value):
        return value >= 0

    @property
    def needs_increase(self):
        return self._needs_increase

    @needs_increase.setter
    def needs_increase(self, value):
        if not Supply.__are_new_needs_valid(value):
            raise ValueError('Needs increase cannot be less than zero.')

        self._needs_increase = value

    def apply(self, survivor: Survivor):
        survivor.needs += self._needs_increase
