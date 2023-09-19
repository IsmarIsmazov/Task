from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from apps.task.filters import TaskFilter
from apps.task.models import Task, Category
from apps.task.serializers import TaskSerializer, CategorySerializer


# Create your views here.
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_class = TaskFilter
    filter_backends = [DjangoFilterBackend]
    ordering_fields = ['priority', 'created_at']
    search_fields = ['title', 'description']


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
