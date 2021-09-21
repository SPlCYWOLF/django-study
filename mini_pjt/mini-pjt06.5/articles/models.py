from django.db import models
# Create your models here.

class Article(models.Model):
    
    champion_name = models.CharField(max_length=50)
    description = models.TextField()
    picture = models.ImageField(blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.champion_name}'