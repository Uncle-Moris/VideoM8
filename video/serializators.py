from rest_framework import serializers
from video.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'stars', 'user', 'movie')