from django.shortcuts import render, get_object_or_404
from .models import Song

def home(request):
    songs = Song.objects.all()
    return render(request, 'music/home.html', {'songs': songs})

def player_view(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'music/player.html', {'song': song})
