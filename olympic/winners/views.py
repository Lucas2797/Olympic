from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from winners.models import *
from winners.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



def home_view (request):
    if request.method == 'GET':
        return JsonResponse(reverse('player_list', safe=False))
        
        
@api_view(['GET', 'POST'])
def player_list(request):
    
    if request.method == 'GET':
        query = Player.objects.all()
        seri = PlayerSerializer(query, many=True)
        return JsonResponse(seri.data, safe=False)
    
    elif request.method == 'POST':
        seri = PlayerSerializer(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(seri.errors, status=400)
            
            
@csrf_exempt      
def event_list(request):
    if request.method == 'GET':
        query = Event.objects.all()
        seri = EventSerializer(query, many=True)
        return JsonResponse(seri.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        seri = EventSerializer(data=data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(seri.errors, status=400)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT'])
def player_detail(request, id):
    try:
        obj = Player.objects.get(id=id)
    except Player.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        seri = PlayerSerializer(obj)
        return JsonResponse(seri.data)
    
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
        return JsonResponse(seri.data)
    
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
        


