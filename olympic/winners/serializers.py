from .models import *
from rest_framework import serializers
from .models import Player




class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    winner = serializers.HyperlinkedRelatedField(many=True, view_name='event-detail', queryset=Event.objects.all())
    link = serializers.HyperlinkedIdentityField(view_name='player_detail', format='api')
    class Meta:
        model = Player
        fields = ['id',  'player_id', 'name', 'winner', 'link', 'sex', 'age', 'height', 'weight', 'team']
        
        
class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['winner', 'noc', 'games', 'year', 'city', 'season', 'sport']