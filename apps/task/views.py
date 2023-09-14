from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.task.models import Task, Hashtag
from apps.task.serializers import TaskSerializer, HashtagSerializer


# Create your views here.
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class HashtagViewSet(ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
