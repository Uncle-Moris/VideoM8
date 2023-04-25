# from django.shortcuts import render
from rest_framework import viewsets
from .models import TblMovies
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    RAWSQL = """SELECT * FROM public.tbl_movies WHERE link_to_the_movie IS NOT NULL
    ORDER BY stripped_title;"""

    # queryset = TblMovies.objects.raw(RAWSQL)

    queryset = TblMovies.objects.filter(link_to_the_movie__isnull=False).order_by('stripped_title')
    serializer_class = MovieSerializer
