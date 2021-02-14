from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from winners.models import *
from winners.serializers import *



def home_view (request):
    if request.method == 'GET':
        return JsonResponse(reverse('player_list', safe=False))
        
@csrf_exempt
def player_list(request):
    
    if request.method == 'GET':
        query = Player.objects.all()
        seri = PlayerSerializer(query, many=True)
        return JsonResponse(seri.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        seri = PlayerSerializer(data=data)
        if seri.is_valid():
            p1 = Player(**seri.validated_data)
            p1.save()
            return reverse('player_detail', p1.id)
        
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
            e1 = Event(**seri.validated_data)
            e1.save() 

        else:
            return JsonResponse(seri.errors, status=400)

@csrf_exempt
def player_detail(request, id):
    try:
        obj = Player.objects.get(id=id)
    except Player.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        seri = PlayerSerializer(obj)
        return JsonResponse(seri.data)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        seri = PlayerSerializer(obj, data=data)
        if seri.is_valid():
            seri.save()
            return JsonResponse(seri.data)
        
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
        data = JSONParser().parse(request)
        seri = EventSerializer(obj, data=data)
        if seri.is_valid():
            seri.save()
            return JsonResponse(seri.data)
        
    if request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)
        


