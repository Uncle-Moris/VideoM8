from django.contrib import admin
from .models.models import *


class BasicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Video)