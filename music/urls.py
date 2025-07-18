from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Or whatever view you want to show
]
