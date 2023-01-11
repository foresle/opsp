import json
from django.views.generic import TemplateView

from .models import Map


class MapView(TemplateView):
    template_name = 'map/map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _map = Map.objects.all().order_by('updated_at').last()

        if _map is not None:
            context['map'] = json.dumps(_map.map)
        else:
            context['map'] = json.dumps({})

        return context
