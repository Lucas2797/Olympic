from .models import *
from rest_framework import serializers




class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['player_id', 'name', 'sex', 'age', 'height', 'weight', 'team']
        
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['winner', 'noc', 'games', 'year', 'city', 'season', 'sport', 'medal']