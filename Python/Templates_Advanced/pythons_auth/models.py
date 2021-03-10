from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    date_of_birthday = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to='public/images')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# Create your models here.
