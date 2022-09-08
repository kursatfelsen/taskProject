import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializers import TaskSerializer


class TaskListApiView(APIView):
    def get(self, request, *args, **kwargs):

        tasks = Task.objects.filter(is_active=True)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        data = {
            'title': request.data.get('title'),
            'is_completed': request.data.get('is_completed'),
            'last_updated': datetime.datetime.now(),
            'is_active': False if request.data.get('is_active') == 'false' else True
        }
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailApiView(APIView):

    def get_object(self, task_id):
        try:
            return Task.objects.get(id=task_id, is_active=True)
        except Task.DoesNotExist:
            return None

    def get(self, request, task_id, *args, **kwargs):

        task_instance = self.get_object(task_id)
        if not task_instance:
            return Response(
                {"res": "Object with task id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TaskSerializer(task_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, task_id, *args, **kwargs):

        task_instance = self.get_object(task_id)
        if not task_instance:
            return Response(
                {"res": "Object with task id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'),
            'is_completed': request.data.get('is_completed'),
            'last_updated': datetime.datetime.now(),
            'is_active': False if request.data.get('title') == 'false' else True
        }
        serializer = TaskSerializer(instance=task_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id, *args, **kwargs):

        task_instance = self.get_object(task_id)
        if not task_instance:
            return Response(
                {"res": "Object with task id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        task_instance.is_active = False
        task_instance.save()

        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )