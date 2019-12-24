from django.db import models
from random_string import random_gen

# Create your models here.
class URLS(models.Model):
    url = models.CharField(max_length=500)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.code} - {self.url}'
    
    class Meta:
        ordering = ['code','url']