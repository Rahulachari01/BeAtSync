from django.urls import path
from . import views

urlpatterns = [
    # This line sends the main page URL ('') to the 'home' view
    path('', views.home, name='home'),
]