from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from apps.notifications.utils import send_task_notification
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

    def perform_create(self, serializer):
        task = serializer.save()
        content = f"Создана новая задача '{task.title}'."
        send_task_notification(task, content)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
