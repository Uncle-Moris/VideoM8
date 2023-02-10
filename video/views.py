from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models.models import Movie, Category, Actor, Director


class VideoList(ListView):
    model = Movie
    context_object_name = 'video'
    template_name = "video/lists/movie_list.html"


class VideoDetail(DetailView):
    model = Movie
    template_name = "video/details/video_details.html"
    context_object_name = "video"


class CategoriesList(ListView):
    model = Category
    template_name = "video/lists/categories_list.html"
    context_object_name = "categories"


class CategoriesDetail(DetailView):
    model = Category
    template_name = ""


class ActorsList(ListView):
    model = Actor
    template_name = "video/lists/actors_list.html"


class ActorsDetail(DetailView):
    model = Actor
    template_name = ""


class DirectorsList(ListView):
    model = Director
    template_name = "video/lists/directors_list.html"


class DirectorsDetails(DetailView):
    model = Director
    template_name = ""
