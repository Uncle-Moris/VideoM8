from django.contrib import admin
from .models.models import Category, Actor, Director, Movie


class BasicAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    readonly_fields = ('slug', )
    #prepopulated_fields = {'slug': ('name', )}


class MovieAdmin(BasicAdmin):
    list_filter = ('director', )
    search_fields = ('director__name', 'name')
    filter_horizontal = ['actors', 'categories']


admin.site.register(Category, BasicAdmin)
admin.site.register(Actor, BasicAdmin)
admin.site.register(Director, BasicAdmin)
admin.site.register(Movie, MovieAdmin)
