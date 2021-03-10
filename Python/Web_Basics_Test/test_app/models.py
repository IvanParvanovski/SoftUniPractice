from django.db import models


class FormTest(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    CAR_CHOICES = (
        ('B', 'BMW'),
        ('A', 'Audi')
    )
    comment = models.TextField(blank=False)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES)
    cars = models.CharField(max_length=30, choices=CAR_CHOICES)

# Create your models here.
