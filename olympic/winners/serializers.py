from .models import *
from rest_framework import serializers




class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['id',  'player_id', 'name', 'sex', 'age', 'height', 'weight', 'team']
        
        
class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['winner', 'noc', 'games', 'year', 'city', 'season', 'sport']