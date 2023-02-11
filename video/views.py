from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models.models import Movie, Category, Actor, Director
from django.db.models import Q

class VideoList(ListView):
    model = Movie
    context_object_name = 'video'
    template_name = "video/lists/movie_list.html"

    def get_queryset(self):
        category = self.kwargs.get('category')
        actor = self.kwargs.get('actor')
        director = self.kwargs.get('director')

        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |

                Q(actors__name__icontains=search_query) |

                Q(director__name__icontains=search_query) |
                Q(categories__name__icontains=search_query)
            )

        if category:
            queryset = queryset.filter(categories__name__icontains=category)

        if actor:
            queryset = queryset.filter(actors__name__icontains=actor)

        if director:
            queryset = queryset.filter(director__name__icontains=director)

        return queryset


class VideoDetail(DetailView):
    model = Movie
    template_name = "video/details/video_details.html"
    context_object_name = "video"


class CategoriesList(ListView):
    model = Category
    template_name = "video/lists/categories_list.html"
    context_object_name = "categories"


# class CategoriesDetail(DetailView):
#     model = Category
#     template_name = ""


class ActorsList(ListView):
    model = Actor
    template_name = "video/lists/actors_list.html"
    context_object_name = "actors"

# class ActorsDetail(DetailView):
#     model = Actor
#     template_name = ""


class DirectorsList(ListView):
    model = Director
    template_name = "video/lists/directors_list.html"
    context_object_name = "directors"

# class DirectorsDetails(DetailView):
#     model = Director
#     template_name = ""
