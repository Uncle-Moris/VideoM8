from factory.django import DjangoModelFactory
from factory import LazyAttribute, LazyFunction, Factory

from video.models.models import (
    Movie,
    Category,
    Actor,
    Director
)

from faker import Faker


fake = Faker()


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = fake.name()


class ActorFactory(DjangoModelFactory):
    class Meta:
        model = Actor

    name = fake.name()


class DirectorFactory(DjangoModelFactory):
    class Meta:
        model = Director

    name = fake.name()


class MovieFactory(DjangoModelFactory):
    class Meta:
        model = Movie
