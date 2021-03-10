from django.db import models


class Demo(models.Model):
    name = models.CharField(max_length=30, blank=False)
    age = models.PositiveIntegerField(blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=30, blank=False)
    text = models.TextField(blank=False)
    size = models.IntegerField(blank=False, default=1)
