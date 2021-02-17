from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('player_list/', views.player_list, name='player_list'),
    path('event_list/', views.event_list, name='event_list'),
    path('player_detail/<int:id>/', views.player_detail, name='player_detail'),
    path('event_detail/<int:id>/', views.event_detail, name='event_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html', 'csv'])
