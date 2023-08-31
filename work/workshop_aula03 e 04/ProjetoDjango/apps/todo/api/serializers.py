from rest_framework import serializers

from apps.todo.models import task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        
        fields = ["name", "description", "date"]

