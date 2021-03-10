from abc import ABC, abstractmethod

from django.core.exceptions import ValidationError


class DataValidator(ABC):
    @abstractmethod
    def __init__(self, exception_message):
        self.exception_message = exception_message

    @abstractmethod
    def validate(self, value):
        pass

    def error(self, message_continue):
        return f'{self.exception_message}\n' \
               f'{message_continue}'


class EgnValidator(DataValidator):
    def __init__(self, exception_message):
        super().__init__(exception_message)

    @staticmethod
    def does_egn_contain_only_digits(value):
        return value.isnumeric()

    def validate(self, value):
        if not EgnValidator.does_egn_contain_only_digits(value):
            raise ValidationError(self.error('The value should contain only digits!'))

        return value
