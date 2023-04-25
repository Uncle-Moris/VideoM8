from rest_framework import serializers
from .models import TblMovies


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblMovies
        fields = ['pk',
                  'main_title',
                  'stripped_title',
                  'link_to_the_movie']
