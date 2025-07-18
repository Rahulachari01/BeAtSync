# music/models.py
from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='songs/')
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return self.title
