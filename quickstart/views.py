from rest_framework.response import Response
from . models import TempModel
from rest_framework import viewsets, serializers
from . serializers import TempModelSerializer
from django.http import HttpResponse
import requests
import pytemperature




class TempModelViewSet(viewsets.ModelViewSet):
    queryset = TempModel.objects.all()
    serializer_class = TempModelSerializer
    def get_paginated_response(self, data):
        return Response(data)



def search(request):
    if 't' in request.GET:
        api_url = 'http://127.0.0.1:8000/temperatures/'
        res = requests.get(api_url)
        data = res.json() #получаем список дат
        for c in data:
            if request.GET['t'] in c['date']:
                if 'g' in request.GET:
                    if request.GET['g'] == 'f':
                        return HttpResponse(pytemperature.c2f(c['temperature']))#Фаренгейты
                    elif request.GET['g'] == 'k':
                        return HttpResponse(pytemperature.c2k(c['temperature']))#Кельвины
                return HttpResponse(c['temperature'])
    return HttpResponse('empty request')


