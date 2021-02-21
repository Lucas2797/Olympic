from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from winners.models import *
from winners.serializers import *
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from .models import Player, Event
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer

        
        
class HomeView(APIView):
    template_name = 'home.amp.html'
    
        
        
        
@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer])
def home_view (request, format=None):
    if request.method == 'GET':
        link1 = reverse('player_list', request=request, format=format)
        link2 = reverse('event_list', request=request, format=format)
        context = {
            'link1': link1,
            'link2': link2,
        }
        return Response(context, template_name='home.amp.html')

    
@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer])
def player_list(request, format=None):
    
    if request.method == 'GET':
        query = Player.objects.all()
        seri = PlayerSerializer(query, many=True, context = {'request':request})
        return Response(seri.data, template_name='winner_list.amp.html')
    
    elif request.method == 'POST':
        seri = PlayerSerializer(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seri.errors, status=400)

   
@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer]) 
def event_list(request):
    if request.method == 'GET':
        query = Event.objects.all()
        seri = EventSerializer(query, many=True, context = {'request':request})
        return Response(seri.data, template_name='event_list.amp.html')
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        seri = EventSerializer(data=data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def player_detail(request, pk):
    try:
        obj = Player.objects.get(pk=pk)
    except Player.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        seri = PlayerSerializer(obj, context={'request': request})
        return Response(status=status.HTTP_200_OK, data=seri.data)
    
    if request.method == 'PUT':
        seri = PlayerSerializer(obj, data=request.data, context={'request': request})
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(seri.errors, status=status.HTTP_304_NOT_MODIFIED)
        
    if request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt      
def event_detail(request, pk):
    try:
        obj = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        seri = EventSerializer(obj, context={'request': request})
        return Response(data=seri.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        seri = EventSerializer(obj, data=request.data, context={'request': request})
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(seri.errors, status=status.HTTP_304_NOT_MODIFIED)
        
    if request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)
        






class PlayerList(APIView):
    
    def get(self, request, format=None):
        query = Player.objects.all()
        seri = PlayerSerializer(query, many=True, context={'request':request})
        return Response(seri.data, status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request, format=None):
        seri = PlayerSerializer(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=status.HTTP_201_CREATED)
        return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)




class PlayerDetail(APIView):
    def get_object(self, pk):
        try:
            return Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        t1 = self.get_object(pk)
        seri = PlayerSerializer(t1)
        return Response(status=status.HTTP_200_OK, data=seri.data)

    def put(self, request, pk, format=None):
        t1 = self.get_object(pk)
        seri = PlayerSerializer(t1, data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
        return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)


class EventList(APIView):
    
    def get(self, request, format=None):
        query = Event.objects.all()
        seri = EventSerializer(query, many=True, context={'request':request})
        return Response(seri.data, status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request, format=None):
        seri = EventSerializer(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=status.HTTP_201_CREATED)
        return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class EventDetail(APIView):
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        t1 = self.get_object(pk)
        seri = EventSerializer(t1)
        return Response(status=status.HTTP_200_OK, data=seri.data)

    def put(self, request, pk, format=None):
        t1 = self.get_object(pk)
        seri = EventSerializer(t1, data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
        return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)