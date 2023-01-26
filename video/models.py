from django.db import models


class BasicModel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(BasicModel):

    class Meta:
        ordering = ['name']


class Video(models.Model):
    title = models.CharField(max_length=255, unique=True)
    #year
    video = models.FileField(upload_to="video/%y")
    miniature = models.ImageField(null=True)
    rating = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=5)
    #+ _rt
    #rating_imdb = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=5)
    description = models.TextField(max_length=1000, null=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
