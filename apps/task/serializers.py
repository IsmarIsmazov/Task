from rest_framework.serializers import ModelSerializer

from apps.task.models import Task, Category


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
