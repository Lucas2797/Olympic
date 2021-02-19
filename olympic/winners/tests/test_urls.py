from django.urls import resolve, reverse


class TestUrls():

    def test_player_list(self):
        path = reverse('player_list')
        assert resolve(path).view_name == 'player_list'
        assert resolve(path)._func_path == 'winners.views.player_list'
        assert resolve(path).route == 'winners/player_list/'

    def test_player_detail(self):
        path = reverse('player_detail', kwargs={'id': 1})
        assert resolve(path).view_name == 'player_detail'
        assert resolve(path)._func_path == 'winners.views.player_detail'
        assert resolve(path).route == 'winners/player_detail/<int:id>/'

    def test_event_list(self):
        path = reverse('event_list')
        assert resolve(path).view_name == 'event_list'
        assert resolve(path)._func_path == 'winners.views.event_list'
        assert resolve(path).route == 'winners/event_list/'

    def test_event_detail(self):
        path = reverse('event_detail', kwargs={'id': 1})
        assert resolve(path).view_name == 'event_detail'
        assert resolve(path)._func_path == 'winners.views.event_detail'
        assert resolve(path).route == 'winners/event_detail/<int:id>/'
