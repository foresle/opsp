from django.contrib import admin
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget

from .models import Bot


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
