from django.contrib import admin

from .models import Map


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('updated_at',)
