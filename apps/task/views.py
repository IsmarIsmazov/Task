from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from apps.task.filters import TaskFilter
from apps.task.models import Task, Hashtag
from apps.task.serializers import TaskSerializer, HashtagSerializer


# Create your views here.
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_class = TaskFilter
    filter_backends = [DjangoFilterBackend]
    ordering_fields = ['priority', 'created_at']
    search_fields = ['title', 'description']


class HashtagViewSet(ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
