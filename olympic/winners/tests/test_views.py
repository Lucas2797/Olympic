from rest_framework.reverse import reverse
import requests



class TestView():
    
    data={
        'player_id': 123452,
        'name':'lucas45',
        'sex':'M',
        'age':21,
        'height':1,
        'weight':1,
        'team':'google'
    }


    def test_formats(self):
        r1 = requests.get('http://127.0.0.1/winners/player_list/?format=json', self.data)
        assert r1.status_code == 200
        assert r1.headers['Content-Type'] == 'application/json'
        r1 = requests.get('http://127.0.0.1/winners/player_list/?format=api', self.data)
        assert r1.headers['Content-Type'] == 'text/html; charset=utf-8'
        r1 = requests.get('http://127.0.0.1/winners/player_list/', self.data)
        assert r1.headers['Content-Type'] == 'text/html; charset=utf-8'
        
    



        
        # r3 = requests.delete('http://127.0.0.1/winners/player_detail/{}/'.format(json.loads(r1._content)['id']))
        # assert r3.status_code == 204
        # r4 = requests.post('http://127.0.0.1/winners/player_list/', data)
        # assert r4.status_code == 201
        # r5 = requests.delete('http://127.0.0.1/winners/player_detail/{}/'.format(json.loads(r4._content)['id']))
        # assert r5.status_code == 204



    
    # def test_profile_view_authenticated(self, client):
    #     # crio um profile#
    #     # assimilo a url do profile#
    #     path = reverse('profile', kwargs={'pk': p1.id})
    #     # fez o request e recebeu o response sem logar status_code=302#
    #     response =  client.get(path)
    #     # aqui logo#
    #     response.user = p1.user
    #     # status_code agora e 200#
    #     response2 = views.profile_view(response, pk=p1.id)
    #     assert response.status_code == 302
    #     assert response2.status_code == 200
    #     assert response.streaming == False
    #     assert response.charset == 'utf-8'
    #     assert response.close() == None
