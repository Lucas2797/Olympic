import requests
from django.core.exceptions import ValidationError
import sys
import pytest
import json

print(sys.path)
from winners.models import Player




        
@pytest.mark.django_db
class TestModels():
    def test_create(self, client):
        data={
            'player_id': 22222,
            'name':'lucas45',
            'sex':'M',
            'age':21,
            'height':1,
            'weight':1,
            'team':'google',
            'wrong': False,
        }
        r1 = requests.post('http://127.0.0.1/winners/player_list.json/', data)
        assert r1.status_code == 201
        r2 = requests.post('http://127.0.0.1/winners/player_list/', data)
        assert r2.status_code == 500
        r3 = requests.delete('http://127.0.0.1/winners/player_detail/{}/'.format(json.loads(r1._content)['id']))
        assert r3.status_code == 204
        r4 = requests.post('http://127.0.0.1/winners/player_list.json/', data)
        assert r4.status_code == 201
        r5 = requests.delete('http://127.0.0.1/winners/player_detail/{}/'.format(json.loads(r4._content)['id']))
        assert r5.status_code == 204



