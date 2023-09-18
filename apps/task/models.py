from django.db import models
class Hashtag(models.Model):
    title = models.CharField(max_length=100)

class Task(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    completed = models.BooleanField()
    hashtag = models.ManyToManyField(Hashtag,)
