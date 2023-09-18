import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
    created_at__lt = django_filters.DateFilter(field_name='created_at', lookup_expr='lt')
    created_at__gt = django_filters.DateFilter(field_name='created_at', lookup_expr='gt')

    class Meta:
        model = Task
        fields = ["created_at__gt", 'created_at__lt', 'title', 'descriptions', 'completed']
