from django.urls import path, include

from rest_framework import routers

from apps.todo.api.viewsets import Taskviewset

router = routers.DefaultRouter()

router.register("", Taskviewset, basename="task")

urlpatterns = [
    path("",include(router.urls)),    
]
