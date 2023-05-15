# from django.shortcuts import render
from rest_framework import viewsets
from .models import TblMovies
from .serializers import MovieSerializer
from django.views.generic import ListView, DetailView


class MovieListView(ListView):
    model = TblMovies
    template_name = 'movies/movie_list.html'#loc of this template is backend/videom8/templates/movies/movie_list.html

    context_object_name = 'movies'
    ordering = ['stripped_title']

    def get_queryset(self):
        return TblMovies.objects.filter(link_to_the_movie__isnull=False).order_by('stripped_title')

class MovieDetailView(DetailView):
    model = TblMovies
    template_name = 'movies/movie_detail.html'#loc of this template is backend/videom8/templates/movies/movie_detail.html

    context_object_name = 'movie'

    def get_queryset(self):
        return TblMovies.objects.filter(link_to_the_movie__isnull=False).order_by('stripped_title')


class MovieViewSet(viewsets.ModelViewSet):
    RAWSQL = """SELECT * FROM public.tbl_movies WHERE link_to_the_movie IS NOT NULL
    ORDER BY stripped_title;"""

    # queryset = TblMovies.objects.raw(RAWSQL)

    queryset = TblMovies.objects.filter(link_to_the_movie__isnull=False).order_by('stripped_title')
    serializer_class = MovieSerializer
