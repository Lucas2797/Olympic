from django.db import models
import sys
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError

M = 'M'
F = 'F'
NA = 'NA'


sex_choices = [
    (M, 'M'),
    (F, 'F'),
    (NA, 'NA'),
]

Summer = 'Summer'
Winter = 'Winter'

season_choices = [
    (Summer, 'Summer'),
    (Winter, 'Winter'),
]


    
    
    
class Player (models.Model):
    player_id = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=2, choices=sex_choices)
    age = models.PositiveIntegerField(null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    team = models.CharField(max_length=120)
    wrong = models.BooleanField(default=False)

    
    def __str__(self):
        return '%s %s' % (self.player_id, self.name)
    
    
    def save(self, *args, **kwargs):
        try:
            o1 = Player.objects.get(player_id=self.player_id, age=self.age, wrong=self.wrong, height=self.height, weight=self.weight, team=self.team, name=self.name)
            raise ValidationError('Player already in')
        except ObjectDoesNotExist:
            super().save(*args, **kwargs)
        
    
class Event(models.Model):
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='events')
    noc = models.CharField(max_length=3)
    games = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    city = models.CharField(max_length=50)
    season = models.CharField(max_length=6, choices=season_choices)
    sport = models.CharField(max_length=50)
    medal = models.CharField(max_length=50)
    wrong = models.BooleanField(default=False)

    
    def __str__(self):
        return '%s %s' % (self.games, self.season) 