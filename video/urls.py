from django.urls import path
from .views import *

urlpatterns = [
    path('', VideoList.as_view(), name='video-list'),
    #path('movies/', VideoList.as_view(), name='video-list'),
    path('movies/<slug:slug>/',  VideoDetail.as_view(), name='video-detail'),


    path('categories/', CategoriesList.as_view(), name='categories-list'),
    path('categories/movies/<str:category>', VideoList.as_view(), name='video-list-categories'),



    path('actors/', ActorsList.as_view(), name='actors-list'),
    path('actors/movies/<str:actor>', VideoList.as_view(), name='video-list-actors'),

    path('directors/', DirectorsList.as_view(), name='directors-list'),
    path('directors/movies/<str:director>', VideoList.as_view(), name='video-list-directors')
]
