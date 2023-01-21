from django.contrib import admin

from .models import Tip


@admin.register(Tip)
class AdminTip(admin.ModelAdmin):
    list_display = ('category', 'text')
