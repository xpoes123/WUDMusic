from django.db import models

class Concert(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing integer ID
    name = models.CharField(max_length=255)  # Name of the concert
    date = models.DateTimeField()  # Date and time of the show
    venue = models.CharField(max_length=255)  # Location of the venue
    description = models.TextField()  # Description of the concert
    spotify = models.URLField(blank=True, null=True)  # Link to Spotify
    instagram = models.URLField(blank=True, null=True)  # Link to Instagram
    image = models.ImageField(upload_to='concert_images/')  # Image of the concert

    def __str__(self):
        return f"{self.name} at {self.venue} on {self.date}"
