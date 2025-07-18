from django.db import models

class Song(models.Model):
    # These lines MUST be indented with 4 spaces
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='songs/')

    # This function and its contents MUST also be indented
    def __str__(self):
        return self.title