from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet, MovieListView, MovieDetailView

# router = routers.DefaultRouter()
# router.register('movies', MovieViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', MovieListView.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]