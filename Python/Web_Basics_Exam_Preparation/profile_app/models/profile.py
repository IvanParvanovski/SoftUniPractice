from django.db import models

from profile_app.validators import validate_does_not_contain_spaces


class Profile(models.Model):
    first_name = models.CharField(max_length=15, validators=(validate_does_not_contain_spaces,))
    last_name = models.CharField(max_length=15)
    budget = models.IntegerField()
