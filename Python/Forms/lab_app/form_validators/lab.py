from django.forms import forms
from abc import ABC, abstractmethod


class DataValidator(ABC):
    @abstractmethod
    def __init__(self, error_message):
        self.error_message = error_message

    @abstractmethod
    def validate(self, value):
        pass


class NameValidator(DataValidator):
    def __init__(self):
        name_error_message = 'The name must start with an uppercase letter.'
        super().__init__(name_error_message)

    @staticmethod
    def does_name_start_with_uppercase_letter(value:str):
        return value[0].isupper()

    def validate(self, value):
        if not NameValidator.does_name_start_with_uppercase_letter(value):
            raise forms.ValidationError(self.error_message)


class AgeValidator(DataValidator):
    def __init__(self):
        age_error_message = 'The age cannot be less than zero.'
        super().__init__(age_error_message)

    def validate(self, value):
        if not NameValidator.does_name_start_with_uppercase_letter(value):
            raise forms.ValidationError(self.error_message)


class EmailValidator(DataValidator):
    def __init__(self):
        email_error_message = 'Enter a valid email.'
        super().__init__(email_error_message)

    def validate(self, value):
        if not NameValidator.does_name_start_with_uppercase_letter(value):
            raise forms.ValidationError(self.error_message)


class PasswordValidator(DataValidator):
    def __init__(self):
        password_error_message = 'Enter a valid password.'
        super().__init__(password_error_message)


    def validate(self, value):
        if not NameValidator.does_name_start_with_uppercase_letter(value):
            raise forms.ValidationError(self.error_message)

