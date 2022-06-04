from rest_framework import serializers

from tasks_model.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"



class QueryParamSerializer(serializers.Serializer):
    status = serializers.ListField(
        child=serializers.ChoiceField(choices=Task.Status.choices), required=False,
    )

