from unittest import TestCase

from django.core.exceptions import ValidationError

from testing.validators import EgnValidator


class EgnValidatorTests(TestCase):
    def setUp(self):
        error_msg = 'Invalid data: '
        self.validator = EgnValidator(error_msg)

    def test_egnValidatorValidate_whenEgnIsValid_shouldReturnEgn(self):
        egn = '1234567890'
        result = self.validator.validate(egn)

        self.assertIsNotNone(result)

    def test_egnValidatorValidate_whenEgnContainLetters_shouldRaiseValidationErrorWithRightMessage(self):
        egn = '1234567a90'

        with self.assertRaises(ValidationError) as context:
            self.validator.validate(egn)

        self.assertIsNotNone(context)
        self.assertEqual(context.exception.message, 'Invalid data: \nThe value should contain only digits!')

    def test_egnValidatorValidate_whenEgnIsEmpty_shouldRaiseValidationErrorWithRightMessage(self):
        egn = ''

        with self.assertRaises(ValidationError) as context:
            self.validator.validate(egn)

        self.assertIsNotNone(context)
        self.assertEqual(context.exception.message, 'Invalid data: \nThe value should contain only digits!')
