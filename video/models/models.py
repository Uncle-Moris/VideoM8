from django.db import models
from .abstract_models import BasicModel


class Category(BasicModel):
    pass


class Actor(BasicModel):
    pass


class Director(BasicModel):
    pass


class Video(BasicModel):
    premiere = models.DateField()
    video = models.FileField(upload_to="video/", null=False)
    miniature = models.ImageField(upload_to="miniatures/", null=True)
    rating = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=5)
    description = models.TextField(max_length=2000, null=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)
    actors = models.ManyToManyField(Actor)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
