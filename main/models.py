from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    Genre = (
        ('comedy', 'comedy'),
        ('action', 'action'),
        ('drama', 'drama'),
    )
    title = models.CharField(max_length=100)
    year = models.DateField()
    runtime = models.FloatField()
    genre = models.CharField(max_length=25, choices=Genre)
    actors = models.ForeignKey(Actor, on_delete=models.CASCADE)
    description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to="media")

    def __str__(self):
        return self.title
