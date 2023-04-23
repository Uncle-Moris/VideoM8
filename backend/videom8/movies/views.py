# from django.shortcuts import render
from rest_framework import viewsets
from .models import TblMovies
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = TblMovies.objects.all()
    serializer_class = MovieSerializer
