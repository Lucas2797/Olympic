from django.core.management.base import BaseCommand
from ...models import Player, Event
from django.core.exceptions import ObjectDoesNotExist



class Command(BaseCommand):

    def listing(self, champ, n):
        medal_choices = ['Gold', 'Silver', 'Bronze', 'NA', 0]
        lista = champ.split(',')
        if len(lista) >= 16:
            lista.remove(lista[14])
        one = lista[n].replace('"', '').replace('NA', '0')
        #return champ[1:].split(',')[n].replace('"', '')
        return one

    def medal_func(self, champ, one):
        medal_choices =['Bronze', 'Gold', 'Silver', 'NA']
        if one in medal_choices:
            return self.listing(champ, 14)
        else:
            try:
                return self.listing(champ, 15)
            except IndexError:
                return self.listing(champ, 14)


    def handle(self, *args, **kwargs):
        all_champs = [row for row in open('athlete_events.csv', 'r')]
        topic = all_champs[0]
        all_champs.remove(all_champs[0])
        for champ in all_champs:  

            p1 = Player(player_id=self.listing(champ, 0),
                        name=self.listing(champ, 1),
                        sex=self.listing(champ, 2),
                        age=self.listing(champ, 3),
                        height=self.listing(champ, 4),
                        weight=self.listing(champ, 5),
                        team=self.listing(champ, 6),
            )
            try:
                obj = Player.objects.get(
                    player_id=p1.player_id,
                    name=p1.name,
                    sex=p1.sex,
                    age=p1.age,
                    height=p1.height,
                    weight=p1.weight,
                    team=p1.team)

                
            except ValueError as e:
                p1.age = 0
                p1.sex = 'M'
                p1.height = 0
                p1.weight = 0
                p1.wrong = True
                p1.save()

                
                
            except ObjectDoesNotExist:
                p1.save()
                try:
                    e1 = Event(
                            noc=self.listing(champ, 7),
                            games=self.listing(champ, 8),
                            year=self.listing(champ, 9),
                            season=self.listing(champ, 10),
                            city=self.listing(champ, 11),
                            sport=self.listing(champ, 12),
                            modality=self.listing(champ,13),
                            medal=self.listing(champ,14),
                            )
                    e1.winner = p1
                    e1.save()
                    print('ok')
                except ValueError:
                    e1.winner = p1
                    e1.year = 0
                    e1.wrong = True
                    e1.modalidality ='wrong'
                    e1.save()






            # p1 = Player("player_{}".format(topic[0].lower().replace('"', ''))==champ.split(',')[0].replace('"', ''),
            #             topic[1].lower().replace('"', '')==champ.split(',')[1],
            #             topic[2].lower().replace('"', '')==champ.split(',')[2],
            #             topic[3].lower().replace('"', '')==champ.split(',')[3].replace('"', ''),
            #             topic[4].lower().replace('"', '')==champ.split(',')[4].replace('"', ''),
            #             topic[5].lower().replace('"', '')==champ.split(',')[5].replace('"', ''),
            # )