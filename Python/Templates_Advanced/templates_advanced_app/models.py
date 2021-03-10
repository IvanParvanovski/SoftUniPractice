from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


def is_zip_validator(value):
    if not value.endswith('.zip'):
        raise ValidationError('Only zip allowed')


class Python(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='public/images')
    snake_passport = models.FileField(upload_to='private/snake_documents',
                                      validators=(is_zip_validator, ))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
