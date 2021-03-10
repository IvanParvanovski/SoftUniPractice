from django.db import models

class Superhero(models.Model):
    name = models.CharField(max_length=100, unique=True)
    secret_identity = models.CharField(max_length=40)

    class Meta:
        pass