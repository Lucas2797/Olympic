from django.urls import resolve, reverse


class TestUrls():

    def test_player_list(self):
        path = reverse('player_list')
        assert resolve(path).view_name == 'player_list'
        assert resolve(path)._func_path == 'winners.views.player_list'
        assert resolve(path).route == 'winners/player_list/'

    def test_player_detail(self):
        path = reverse('player-detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'player-detail'
        assert resolve(path)._func_path == 'winners.views.player_detail'
        assert resolve(path).route == 'winners/player_detail/<int:pk>/'

    def test_event_list(self):
        path = reverse('event_list')
        assert resolve(path).view_name == 'event_list'
        assert resolve(path)._func_path == 'winners.views.event_list'
        assert resolve(path).route == 'winners/event_list/'

    def test_event_detail(self):
        path = reverse('event-detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'event-detail'
        assert resolve(path)._func_path == 'winners.views.event_detail'
        assert resolve(path).route == 'winners/event_detail/<int:pk>/'


