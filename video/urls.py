from django.urls import path
from .views import *

urlpatterns = [
    path('videos/', VideoList.as_view(), name='video-list'),
    path('videos/<slug:slug>/',  VideoDetail.as_view(), name='video-detail')
]
