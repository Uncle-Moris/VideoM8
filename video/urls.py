from django.urls import path
from .views import *

urlpatterns = [
    path('movies/', VideoList.as_view(), name='video-list'),
    path('movies/<slug:slug>/',  VideoDetail.as_view(), name='video-detail')
]
