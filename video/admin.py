from django.contrib import admin
from .models.models import Category, Actor, Director, Movie


class BasicAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, BasicAdmin)
admin.site.register(Actor, BasicAdmin)
admin.site.register(Director, BasicAdmin)
admin.site.register(Movie, BasicAdmin)
