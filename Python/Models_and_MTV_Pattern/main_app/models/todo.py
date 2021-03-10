from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
