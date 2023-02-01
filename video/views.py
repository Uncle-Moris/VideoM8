from django.utils import timezone

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models.models import Movie, Category, Actor, Director


def index(request):
    video = Movie.objects.all()
    return render(request, "video/index.html", {"video": video})


class VideoList(ListView):
    model = Movie
    context_object_name = 'video'


class VideoDetail(DetailView):
    model = Movie
    template_name = "video/video_details.html"
    context_object_name = "video"


class CategoriesList(ListView):
    model = Category
    template_name = "video/categories_list.html"
    context_object_name = "categories"


class CategoriesDetail(DetailView):
    pass


class ActorsList(ListView):
    pass


class ActorsDetail(DetailView):
    pass


class DirectorsList(ListView):
    pass


class DirectorsDetails(DetailView):
    pass
