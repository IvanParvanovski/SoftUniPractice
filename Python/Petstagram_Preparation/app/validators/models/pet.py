from django.core.exceptions import ValidationError

from app.validators.models.mixin import DataValidatorMixIn


class NameValidator(DataValidatorMixIn):
    def __init__(self, error_message):
        super().__init__(error_message)

    @staticmethod
    def does_name_contain_upper_case_letter(value: str) -> bool:
        return any(True for letter in value if letter.isupper())

    @staticmethod
    def does_name_contain_lower_case_letter(value: str) -> bool:
        return any(True for letter in value if letter.islower())

    def validate(self, value):
        if not NameValidator.does_name_contain_upper_case_letter(value):
            raise ValidationError(self.error_message +
                                  'Name should contain upper-case letter.')
