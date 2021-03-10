from Chapter4_Classes_and_OOP.custom_errors.errors.name_validation import NameTooShortError
from Chapter4_Classes_and_OOP.custom_errors.errors_base.base_validation_error import BaseValidationError


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)


name = 'Ivan'

try:
    validate(name)
except BaseValidationError as error:
    raise error

