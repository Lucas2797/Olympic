import sys

from winners.models import Player

sys.path.insert('.')



o1 = Player.objects.all()[0]
print(o1)