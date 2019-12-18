from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    task_duration = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    TODO_TYPE = (
        ('p', 'personal'),
        ('f', 'family'),
        ('h', 'house'),
        ('m', 'misc'),
        ('s', 'school'),
    )

    todo_type = models.CharField(max_length=1, choices=TODO_TYPE, blank=True, default='m')

    class Meta:
        ordering = ['title', 'create_at']
