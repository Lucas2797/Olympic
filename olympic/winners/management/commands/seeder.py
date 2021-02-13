from django.core.management.base import BaseCommand
from ...models import Player, Event



class Command(BaseCommand):
    
    def listing(self, champ, n):
        return champ.split(',')[n].replace('"', '').replace('NA', '0')
    
    def handle(self, *args, **kwargs):
        all_champs = [row for row in open('athlete_events.csv', 'r')]
        topic = all_champs[0]
        all_champs.remove(all_champs[0])
        for champ in all_champs:  
            p1 = Player('player_{}'.format(self.listing(topic, 0).lower())==self.listing(champ, 0),
                        self.listing(topic, 1).lower()==self.listing(champ, 1),
                        self.listing(topic, 2).lower()==self.listing(champ, 2),
                        self.listing(topic, 3).lower()==self.listing(champ, 3),
                        self.listing(topic, 4).lower()==self.listing(champ, 4),
                        self.listing(topic, 5).lower()==self.listing(champ, 5),
                        self.listing(topic, 6).lower()==self.listing(champ, 6),
            )
            if p1 in Player.objects.all():
                print(p1)
                print('ja tem')
            else:
                p1.save()
                e1 = Event(
                        topic[7].lower()==champ[7],
                        topic[8].lower()==champ[8],
                        topic[9].lower()==champ[9],
                        topic[10].lower()==champ[10],
                        topic[11].lower()==champ[11],
                        )
                e1.winner = p1
                e1.save()
                print('ok')






            # p1 = Player("player_{}".format(topic[0].lower().replace('"', ''))==champ.split(',')[0].replace('"', ''),
            #             topic[1].lower().replace('"', '')==champ.split(',')[1],
            #             topic[2].lower().replace('"', '')==champ.split(',')[2],
            #             topic[3].lower().replace('"', '')==champ.split(',')[3].replace('"', ''),
            #             topic[4].lower().replace('"', '')==champ.split(',')[4].replace('"', ''),
            #             topic[5].lower().replace('"', '')==champ.split(',')[5].replace('"', ''),
            # )