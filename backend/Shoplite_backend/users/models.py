from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    numero_telephone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username
    