from django.urls import path
from . import views

app_name = "syncapp"

urlpatterns = [
    path('', views.home, name='home'),
    path('player/<int:song_id>/', views.player_view, name='player'),  # <- This fixes your issue
]
