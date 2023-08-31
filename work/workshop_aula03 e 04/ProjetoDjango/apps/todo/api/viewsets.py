from rest_framework.viewsets import ModelViewSet

from apps.todo.models import task
from .serializers import TaskSerializer

class Taskviewset(ModelViewSet):
    
    queryset = task.objects.all()
    
    serializer_class = TaskSerializer