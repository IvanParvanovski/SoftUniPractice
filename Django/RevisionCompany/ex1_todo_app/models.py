from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=False)
    status = models.BooleanField(default=False)

