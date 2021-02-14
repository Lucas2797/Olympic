from django.contrib import admin
from .models import Player, Event

class PlayerConfig(admin.ModelAdmin):
    list_display = ('player_id', 'name', 'sex', 'age', 'height', 'weight', 'team')
    
class EventConfig(admin.ModelAdmin):
    list_display = ('winner', 'noc', 'games', 'year', 'city', 'season', 'sport', 'medal')
    
admin.site.register(Player, PlayerConfig),
admin.site.register(Event, EventConfig)

