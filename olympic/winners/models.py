from django.db import models


M = 'M'
F = 'F'
NA = 'NA'


sex_choices = [
    (M, 'M'),
    (F, 'F'),
    (NA, 'NA'),
]

Gold = 'Gold'
Silver = 'Silver'
Bronze = 'Bronze'

medal_choices = [
    (Gold, 'Gold'),
    (Silver, 'Silver'),
    (Bronze, 'Bronze')
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
    sex = models.CharField(max_length=9, choices=sex_choices)
    age = models.PositiveIntegerField(null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    team = models.CharField(max_length=120)
    
    def __str__(self):
        return '%s %s' % (self.player_id, self.name) 
    
class Event(models.Model):
    winner = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL, related_name='winner')
    noc = models.CharField(max_length=3)
    games = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    city = models.CharField(max_length=50)
    season = models.CharField(max_length=6, choices=season_choices)
    sport = models.CharField(max_length=50)
    
    def __str__(self):
        return '%s %s' % (self.games, self.season) 