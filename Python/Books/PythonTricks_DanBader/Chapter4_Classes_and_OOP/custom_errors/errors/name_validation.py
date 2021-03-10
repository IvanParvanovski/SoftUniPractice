from Chapter4_Classes_and_OOP.custom_errors.errors_base.base_validation_error import BaseValidationError


class NameTooShortError(BaseValidationError):
    pass


class NameTooLongError(BaseValidationError):
    pass
