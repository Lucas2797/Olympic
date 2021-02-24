from . import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('player_list/', views.player_list, name='player_list'),
    path('player_list/<slug:order>/', views.player_list, name='player_list'),
    path('event_list/', views.event_list, name='event_list'),
    path('event_list/<slug:order>/', views.event_list, name='event_list'),
    path('player_detail/<int:pk>/', views.player_detail, name='player-detail'),
    path('event_detail/<int:pk>/', views.event_detail, name='event-detail'),
    path('api-auth/', include('rest_framework.urls')),
    #class based#
    path('player_list_class/', views.PlayerList.as_view(), name='player_list_class'),
    path('player_detail_class/', views.PlayerDetail.as_view(), name='player_detail_class'),
    path('event_list_class/', views.EventList.as_view(), name='event_list_class'),
    path('event_detail_class/', views.EventDetail.as_view(), name='event_detail_class'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
