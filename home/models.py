from django.db import models

class Concert(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    venue = models.CharField(max_length=255)
    description = models.TextField()
    spotify = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    image = models.ImageField(
        upload_to='concert_images/',
        blank=True,
        null=True,
        default='concert_images/default.jpg'
    )

    def __str__(self):
        return f"{self.name} at {self.venue} on {self.date}"
