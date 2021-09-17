from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    # poster_path = models.CharField(max_length=500)
    image = models.ImageField(blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
