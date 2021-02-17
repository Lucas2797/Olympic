import requests
from django.core.exceptions import ValidationError
import sys
sys.path.append('/home/kali/.virtualenvs/celero/olympic/winners')

print(sys.path)
from models import Player



class TestModels():
    def test_create(self,):
        data={
            'player_id': '2727',
            'name':'lucas',
            'sex':'M',
            'age':21,
            'height':1,
            'weight':1,
            'team':'google'
        }
        r1 = requests.post('http://127.0.0.1/winners/player_list/', data)
        assert r1.status_code == 500
        p1 = Player.objects.get(player_id=2727)
        p1.delete()
        r2 = requests.post('http://127.0.0.1/winners/player_list/', data)
        assert r2.status_code == 201