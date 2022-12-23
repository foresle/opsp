import datetime
import json
import synapse_graph
from django.views.generic import TemplateView
from django.conf import settings
from django.utils import timezone

from .models import Map


class MapView(TemplateView):
    template_name = 'map/map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Update map with timeout in 2 days
        latest_map = Map.objects.all().exclude(updated_at__lt=datetime.datetime.now(tz=timezone.now().tzinfo) - datetime
                                               .timedelta(days=2)).order_by('updated_at').last()

        if latest_map is None:
            try:
                graph = synapse_graph.SynapseGraph(
                    name='matrix.opulus.space',
                    headers={'Authorization': f'Bearer {settings.MATRIX_TOKEN}'},
                    matrix_homeserver='matrix.opulus.space',
                    hide_usernames=True,
                    u2u_relation=False
                )
                new_map = json.loads(graph.json)

                # Clear all unnecessary information
                new_map = {
                    'nodes': new_map['nodes'],
                    'edges': new_map['edges']
                }
                Map.objects.create(map=new_map)
                context['map'] = json.dumps(new_map)

            except synapse_graph.SynapseGraphError:
                context['map'] = json.dumps({'nodes': [], 'edges': []})
        else:
            context['map'] = json.dumps(latest_map.map)

        return context
