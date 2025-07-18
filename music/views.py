from django.shortcuts import render
from .models import Song # Import the Song model

def home(request):
    songs = Song.objects.all() # Get all songs from the database
    context = {'songs': songs} # Create a context dictionary
    return render(request, 'music/index.html', context) # Pass the context to the template