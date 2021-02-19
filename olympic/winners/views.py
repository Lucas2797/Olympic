from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from winners.models import *
from winners.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse



        
@api_view(['GET'])
def home_view (request, format=None):
    if request.method == 'GET':
        link1 = reverse('player_list', request=request, format=format)
        link2 = reverse('event_list', request=request, format=format)
        context = {
            'link1': link1,
            'link2': link2,
        }
        return Response(context)

        
@api_view(['GET', 'POST'])
def player_list(request):
    
    if request.method == 'GET':
        query = Player.objects.all()
        seri = PlayerSerializer(query, many=True, context = {'request':request})
        return Response(seri.data)
    
    elif request.method == 'POST':
        seri = PlayerSerializer(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seri.errors, status=400)
            
            
@csrf_exempt      
@api_view(['GET', 'POST'])
def event_list(request):
    if request.method == 'GET':
        query = Event.objects.all()
        seri = EventSerializer(query, many=True)
        return Response(seri.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        seri = EventSerializer(data=data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seri.errors, status=400)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def player_detail(request, id):
    try:
        obj = Player.objects.get(id=id)
    except Player.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        seri = PlayerSerializer(obj)
        return Response(seri.data)
    
    if request.method == 'PUT':
        seri = PlayerSerializer(obj, data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(seri.errors, status=status.HTTP_304_NOT_MODIFIED)
        
    if request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)
    
@csrf_exempt      
def event_detail(request, id):
    try:
        obj = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        seri = EventSerializer(obj)
        return Response(seri.data)
    
    if request.method == 'PUT':
        seri = EventSerializer(obj, data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(seri.errors, status=status.HTTP_304_NOT_MODIFIED)
        
    if request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)
        


