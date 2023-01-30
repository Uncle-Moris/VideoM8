from django.utils import timezone

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models.models import Movie


def index(request):
    video = Movie.objects.all()
    return render(request, "video/index.html", {"video": video})


class VideoList(ListView):
    model = Movie
    context_object_name = 'video'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class VideoDetail(DetailView):
    model = Movie
    template_name = "video/video_details.html"
    context_object_name = "video"
