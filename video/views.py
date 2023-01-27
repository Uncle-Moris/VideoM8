from django.utils import timezone

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Video


def index(request):
    video = Video.objects.all()
    return render(request, "video/index.html", {"video": video})


class VideoList(ListView):
    model = Video
    context_object_name = 'video'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class VideoDetail(DetailView):
    model = Video
    template_name = "video"