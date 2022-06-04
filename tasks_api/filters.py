from django_filters import rest_framework as filters
from tasks_model.models import Task


class TaskFilter(filters.FilterSet):
    class Meta:
        model = Task
        fields = "__all__"

