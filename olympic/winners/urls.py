from . import views
from django.urls import path



urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('player_list/', views.player_list, name='player_list'),
    path('event_list/', views.event_list, name='event_list'),
    path('player_detail/<int:id>/', views.player_detail, name='player_detail'),
    path('event_detail/<int:id>/', views.event_detail, name='event_detail')
]
