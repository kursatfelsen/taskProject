from django.urls import path, include

from .views import TaskListApiView, TaskDetailApiView

urlpatterns = [
    path('api', TaskListApiView.as_view()),
    path('api/<int:task_id>/', TaskDetailApiView.as_view()),
]