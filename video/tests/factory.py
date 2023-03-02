#import factory
from factory import LazyAttribute, LazyFunction, Factory

from video.models.models import (
    Movie,
    Category,
    Actor,
    Director
)

from faker import Faker


fake = Faker()


class CategoryFactory(Factory):
    class Meta:
        model = Category

    name = fake.name()

class ActorFactory(Factory):
    class Meta:
        model = Actor

    name = fake.name()


class DirectorFactory(Factory):
    class Meta:
        model = Director

    name = fake.name()



class MovieFactory(Factory):
    class Meta:
        model = Movie