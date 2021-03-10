from django.db import models


class Pet(models.Model):
    type = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
