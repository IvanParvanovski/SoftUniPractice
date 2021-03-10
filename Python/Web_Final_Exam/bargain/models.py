from django.db import models

from accounts.models import UserProfile
from watches.models.watch import Watch


class Purchase(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.watch.__str__()}'
