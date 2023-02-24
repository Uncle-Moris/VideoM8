from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .abstract_models import BasicModel
from django.utils.text import slugify


class Category(BasicModel):
    pass


class Actor(BasicModel):
    pass


class Director(BasicModel):
    pass


def user_directory_path(instance, filename):
    return f'video/{filename}'


class Movie(BasicModel):
    premiere = models.DateField()
    video = models.FileField(upload_to=user_directory_path, null=False)
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
    director = models.ForeignKey(Director, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + '-' + str(self.premiere.year))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.premiere.year}"

