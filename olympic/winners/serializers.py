from .models import *
from rest_framework import serializers
from .models import Player, Event



class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(many=True, view_name='event-detail', queryset=Event.objects.all())
    url = serializers.HyperlinkedIdentityField(view_name='player-detail')
    class Meta:
        model = Player
        fields = ['id','events', 'url',  'player_id', 'name', 'sex', 'age', 'height', 'weight', 'team']
        
class EventSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='event-detail')
    class Meta:
        model = Event
        fields = ['winner','id','url', 'noc', 'games', 'year', 'city', 'season', 'sport', 'modality', 'medal']