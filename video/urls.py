from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('movies/', views.VideoList.as_view(), name='video-list'),
    path('movies/<slug:slug>/',  views.DetailI, name='video-detail')
]
