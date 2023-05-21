from django.contrib.admin import register, ModelAdmin

from .models import Phrases


@register(Phrases)
class PhrasesAdmin(ModelAdmin):
    list_display = ['phrase', 'priority']
