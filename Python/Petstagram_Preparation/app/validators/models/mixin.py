from abc import ABC, abstractmethod


class DataValidatorMixIn(ABC):
    @abstractmethod
    def __init__(self, error_message):
        self.error_message = error_message + ' '

    @abstractmethod
    def validate(self, value):
        pass
