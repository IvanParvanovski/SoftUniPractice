from django.db import models

from app.models.pet import Pet


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
