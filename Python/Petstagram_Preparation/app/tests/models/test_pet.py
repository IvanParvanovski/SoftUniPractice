from django.core.exceptions import ValidationError
from django.test import TestCase

from app.models.pet import Pet


class PetModelTests(TestCase):
    def test_createPet_whenDataIsValid_shouldCreateThePet(self):
        type = 'dog'
        name = 'Gigi'
        age = 6
        description = 'Cute dog'
        image_url = 'https://i.insider.com/5484d9d1eab8ea3017b17e29?width=1100&format=jpeg&auto=webp'

        pet = Pet(
            type=type,
            name=name,
            age=age,
            description=description,
            image_url=image_url
        )

        pet.save()

    def test_createPet_whenNameDoesNotContainUpperCaseLetter_shouldRaiseCorrectValidationException(self):
        type = 'cat'
        name = 'gigi'
        age = 6
        description = 'Cute dog'
        image_url = 'https://i.insider.com/5484d9d1eab8ea3017b17e29?width=1100&format=jpeg&auto=webp'

        pet = Pet(
            type=type,
            name=name,
            age=age,
            description=description,
            image_url=image_url
        )

        with self.assertRaises(ValidationError) as context:
            pet.full_clean()
            pet.save()

        self.assertIsNotNone(context.exception)
