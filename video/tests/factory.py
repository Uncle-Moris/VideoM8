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

class MovieFactory(Factory):
    class Meta:
        model = Movie

