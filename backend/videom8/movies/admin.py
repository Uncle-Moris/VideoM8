from django.contrib import admin
from .models import TblMovies

# Register your models here.


@admin.register(TblMovies)
class TblMoviesAdmin(admin.ModelAdmin):
    def get_queryset(self, request):

        return super().get_queryset(request).filter(link_to_the_movie__isnull=False).order_by('stripped_title')
