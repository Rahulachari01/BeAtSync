from django.shortcuts import render
from .models import Song  # Or your actual model name

def home(request):
    songs = Song.objects.all()
    return render(request, 'music/home.html', {'songs': songs})
