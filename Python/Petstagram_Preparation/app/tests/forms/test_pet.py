from django.test import TestCase

from app.forms.pet import PetCreateForm
from app.models.pet import Pet


class TestPetCreateForm(TestCase):
    def test_savePetForm_whenValidData_shouldBeValid(self):
        type = 'dog'
        name = 'Gigi'
        age = 5
        description = 'Amazing dog'
        image_url = 'https://i.insider.com/5484d9d1eab8ea3017b17e29?width=1100&format=jpeg&auto=webp'
        pet = Pet(
            type=type,
            name=name,
            age=age,
            description=description,
            image_url=image_url
        )

        form = PetCreateForm(instance=pet)

        self.assertFalse(form.is_valid())
