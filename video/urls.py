from django.urls import path
from .views import *

urlpatterns = [
    path('movies/', VideoList.as_view(), name='video-list'),
    path('movies/<slug:slug>/',  VideoDetail.as_view(), name='video-detail'),
    path('categories/', CategoriesList.as_view(), name='categories-list'),
    path('categories/<slug:slug>', CategoriesDetail.as_view(), name='categories-detail'),
    path('actors/', ActorsList.as_view(), name='actors-list'),
    path('actors/<slug:slug>', ActorsDetail.as_view(), name='actors-detail'),
    path('directors/', DirectorsList.as_view(), name='directors-list'),
    path('directors/<slug:slug>', DirectorsDetails.as_view(), name='directors-detail')
]
