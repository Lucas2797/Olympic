from django.test import TestCase
import requests
import os
from bs4 import BeautifulSoup




data={
    'player_id': '2727',
    'name':'lucas',
    'sex':'M',
    'age':25,
    'height':1,
    'weight':1,
    'team':'google'
    }
r2 = requests.put('http://45644d9abef4.ngrok.io/winners/player_detail/172/', data=data)

# r1 = requests.post('http://127.0.0.1:80/winners/player_list/', data=data)

# print(data)

with open('test.html', 'a') as file:
    file.write(BeautifulSoup(r2.content, 'html.parser').prettify())

print(r2)