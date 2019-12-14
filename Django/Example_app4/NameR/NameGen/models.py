
from django.conf import settings
from django.db import models

# Create your models here.

class PersonLibrary(models.Model):
    names = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    state = models.CharField(max_length=20)

    # THIS IS THE NAME OF THE OBJECT ELEMENT FACE
    def __str__(self):
            return f'{self.names}, {self.age}'

    def displayPerson(self):
        return f'{self.names} is {self.age} and lives in {self.state}'