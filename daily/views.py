from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters

from .models import Daily


class ListDaily(APIView):
    def get(self, request):
        try:
            daily = Daily.objects.filter(is_open=True).order_by('-date')
            res_list = [
                {
                    'id': d.id,
                    'date': d.date,
                    'evaluation': d.evaluation.evaluation,
                }
                for d in daily
            ]
            return Response(res_list)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DetailDaily(APIView):
    def get(self, request, pk):
        try:
            try:
                daily = Daily.objects.get(id=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            res = {
                'id': daily.id,
                'date': daily.date,
                'study': daily.study,
                'summary': daily.summary,
                'other': daily.other,
            }
            return Response(res)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryDairy(APIView):
    def get(self, request, cat):
        try:
            daily = Daily.objects.filter(is_open=True).values_list(
                'date', cat).order_by('-date')

            res_list = [
                {
                    # 'id': d.id,
                    'date': d[0],
                    'content': d[1],
                }
                for d in daily
            ]

            return Response(res_list) 
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


