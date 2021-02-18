from django.test import TestCase
import requests
import os
from bs4 import BeautifulSoup
from rest_framework.reverse import reverse
import sys
from .models import Player

print(sys.path)



# data={
#     'player_id': '2727',
#     'name':'lucas',
#     'sex':'M',
#     'age':25,
#     'height':1,
#     'weight':1,
#     'team':'google'
#     }


# # # # r1 = requests.post('http://127.0.0.1:80/winners/player_list/', data=data)

# # # # print(r1)

# with open('test.html', 'a') as file:
#     file.write(BeautifulSoup(r2.content, 'html.parser').prettify())
