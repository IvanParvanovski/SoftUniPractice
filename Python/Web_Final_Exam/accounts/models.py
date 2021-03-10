from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    email = models.EmailField(blank=False)
    telephone_number = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='images/users_images/',
                                        default='images/default_pic/default_profile_pic.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
