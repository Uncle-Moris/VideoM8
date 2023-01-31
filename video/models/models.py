from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .abstract_models import BasicModel


class Category(BasicModel):
    pass


class Actor(BasicModel):
    pass


class Director(BasicModel):
    pass


class Movie(BasicModel):
    premiere = models.DateField()
    video = models.FileField(upload_to="video/", null=False)
    miniature = models.ImageField(upload_to="miniatures/", null=True)
    rating = models.DecimalField(max_digits=10,
                                 decimal_places=2,
                                 null=True,
                                 default=False,
                                 validators=(
                                     MinValueValidator(0.0),
                                     MaxValueValidator(10.0))
                                 )
    description = models.TextField(max_length=2000, null=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)
    actors = models.ManyToManyField(Actor)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
