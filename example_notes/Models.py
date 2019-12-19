# MODELS
# This is in the models.py

from django.db import models

# Create models here.

class Article(models.Model):
    # THIS is ALL for one ID.
    # id=1 will have its own title,slug,body,date on one line
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
