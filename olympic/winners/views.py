from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from winners.models import Player, Event
from winners.serializers import PlayerSerializer, EventSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Player, Event
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework import status
from django.db.models import Q


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
def player_list(request, order='player_id' , format=None):
    id_query = request.GET.get('id_query', '')
    name_query = request.GET.get('name_query', '')
    sex_query = request.GET.get('sex_query', '')
    age_query = request.GET.get('age_query', '')
    height_query = request.GET.get('height_query', '')
    weight_query = request.GET.get('weight_query', '')
    team_query = request.GET.get('team_query', '')
    wrong_query = request.GET.get('wrong_query', '')
    filtro_basico = Q(wrong=False)
    if request.method == 'GET':
        if id_query :
            print('id', id_query)
            filtro_basico.add(Q(player_id=id_query), Q.AND)
        if name_query :
            print('name', name_query)
            filtro_basico.add(Q(name__icontains=name_query), Q.AND) 
        if sex_query :
            print('sex')
            filtro_basico.add(Q(sex=sex_query), Q.AND)  
        if age_query :
            print('age')
            filtro_basico.add(Q(age=age_query), Q.AND)  
        if height_query :
            print('height_query', height_query)
            filtro_basico.add(Q(height=height_query), Q.AND)      
        if weight_query :
            print('weight_query', weight_query)
            filtro_basico.add(Q(weight=weight_query), Q.AND)  
        if team_query :
            print('team_query', team_query)
            filtro_basico.add(Q(team=team_query), Q.AND)
    
        query = Player.objects.filter(filtro_basico).order_by(order)
        seri = PlayerSerializer(query, many=True, context={'request': request})
        if request.accepted_renderer.format == 'html':
            context = {
                'query': query,
            }
            return render(request, 'winner_list.amp.html', context)
        else:
            return Response(seri.data, status=status.HTTP_200_OK, template_name='winner_list.amp.html')
    
    elif request.method == 'POST':
        seri = PlayerSerializer(data=request.data, context={'request': request})
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)
   
@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer]) 
def event_list(request, order='winner',format=None):
    winner_query = request.GET.get('winner_query', '')
    noc_query = request.GET.get('noc_query', '')
    games_query = request.GET.get('games_query', '')
    year_query = request.GET.get('year_query', '')
    city_query = request.GET.get('city_query', '')
    season_query = request.GET.get('season_query', '')
    sport_query = request.GET.get('sport_query', '')
    modality_query = request.GET.get('modality_query', '')
    medal_query = request.GET.get('medal_query', '')
    wrong_query = request.GET.get('wrong_query', '')
    filtro_basico = Q(wrong=False)
    if request.method == 'GET':
        if winner_query :
            filtro_basico.add(Q(winner=winner_query), Q.AND)
        if noc_query :
            filtro_basico.add(Q(noc_icontains=noc_query), Q.AND) 
        if games_query :
            filtro_basico.add(Q(games=games_query), Q.AND)  
        if year_query :
            filtro_basico.add(Q(year=year_query), Q.AND)  
        if city_query :
            filtro_basico.add(Q(city=city_query), Q.AND)      
        if sport_query :
            filtro_basico.add(Q(sport=sport_query), Q.AND)  
        if modality_query :
            filtro_basico.add(Q(modality=modality_query), Q.AND)
        if medal_query :
            filtro_basico.add(Q(medal=medal_query), Q.AND)
        if wrong_query :
            filtro_basico.add(Q(wrong=wrong_query), Q.AND)
        query = Event.objects.filter(filtro_basico).order_by(order)
        seri = EventSerializer(query, many=True, context = {'request':request})
        if request.accepted_renderer.format == 'html':
            context = {
                'query': query,
            }
            return render(request, 'event_list.amp.html', context)
        else:
            return Response(seri.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        seri = PlayerSerializer(data=request.data, context={'request': request})
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


        