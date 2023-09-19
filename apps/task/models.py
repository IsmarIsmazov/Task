from django.db import models

from apps.task.constants import PRIORITY_CHOICES
from apps.users.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(auto_created=True)
    completed = models.BooleanField()
    category = models.ManyToManyField(Category)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.title
