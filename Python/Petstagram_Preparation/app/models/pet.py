from django.db import models

from app.validators.models.pet import NameValidator


class Pet(models.Model):
    # First Value is how it will be saved in the database
    # Second Value is how it will be showed to the user

    DOG = 'Dog'
    CAT = 'Cat'
    PARROT = 'Parrot'

    choices = (
        (DOG, 'dog'),
        (CAT, 'cat'),
        (PARROT, 'parrot')
    )

    type = models.CharField(choices=choices,
                            max_length=6,
                            default='',
                            blank=False)

    name = models.CharField(max_length=6,
                            blank=False,
                            validators=(
                                NameValidator('Invalid: ').validate,
                            ))

    age = models.PositiveIntegerField(blank=False)

    description = models.TextField(blank=False)

    image_url = models.URLField(blank=False)
