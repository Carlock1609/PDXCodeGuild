from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    pass
# ADD ADDITIONAL FIELDS HERE

    def __str__(self):
        return self.username