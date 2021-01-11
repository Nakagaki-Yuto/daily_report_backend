from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters

from .models import Task


class ListTask(APIView):
    def get(self, request):
        try:
            task = Task.objects.filter(is_finished=False).order_by('-priority')
            res_list = [
                {
                    'id': t.id,
                    'priority': t.priority,
                    'task': t.task,
                }
                for t in task
            ]
            return Response(res_list)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ListFinishedTask(APIView):
    def get(self, request):
        try:
            task = Task.objects.filter(is_finished=True).order_by('-finished_date')
            res_list = [
                {
                    'id': t.id,
                    'priority': t.priority,
                    'task': t.task,
                    'finished_date': t.finished_date,
                }
                for t in task
            ]
            return Response(res_list)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
