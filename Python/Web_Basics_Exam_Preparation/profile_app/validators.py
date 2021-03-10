from django.core.exceptions import ValidationError


def validate_does_not_contain_spaces(value):
    result = any(True if x == ' ' else False for x in value)
    if result:
        raise ValidationError('Cannot contain white spaces!')
