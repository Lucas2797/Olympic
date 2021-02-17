from rest_framework.reverse import reverse



class TestView():
    def test_home(self):
        assert 2+2==4
    
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
