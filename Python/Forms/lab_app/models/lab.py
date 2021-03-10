from django.db import models


class Lab(models.Model):
    name = models.CharField(blank=False, max_length=30,)
    age = models.PositiveIntegerField(blank=False)
    email = models.EmailField(blank=False,)
    password = models.CharField(blank=False, max_length=30,)
    text = models.TextField(blank=False)
