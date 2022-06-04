from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from . import serializers, filters, permissions
from tasks_model.models import Task

# Create your views here.


class TaskListAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.TaskFilter

    ordering = ["created_at", "importance"]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(public=True)
        return self.order_by_queryset(queryset)

    def filter_queryset(self, queryset):
        return queryset.filter(importance=True)

    def order_by_queryset(self, queryset):
        return queryset.order_by(*self.ordering)


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated | permissions.OnlyAuthorEditNote)
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer


class StatusListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer

    def filter_queryset(self, queryset):
        query_params = serializers.QueryParamSerializer(data=self.request)
        query_params.is_valid(raise_exception=True)
        status_choice = query_params.data.get("status")
        if status_choice:
            queryset = queryset.filter(status__in=query_params.data["status"])
        return queryset
