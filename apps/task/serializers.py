from rest_framework.serializers import ModelSerializer

from apps.task.models import Task, Hashtag


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class HashtagSerializer(ModelSerializer):
    class Meta:
        model = Hashtag
        fields = "__all__"

