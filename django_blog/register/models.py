from django.db import models
from django.contrib.auth.models import AbstractUser

class register(AbstractUser):
    administrador = models.BooleanField(default=False)
