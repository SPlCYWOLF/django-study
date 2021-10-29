from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    actors = models.ManyToManyField(Actor, related_name='movies')       # 이름? / related_name?
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField() 
    poster_path = models.TextField()

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')      # 이름? / related_name?
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.PositiveIntegerField()        # 인자?

    def __str__(self):
        return self.title