import synapse_graph
from celery import shared_task
from django.conf import settings
import json

from .models import Map


@shared_task
def update_map() -> None:
    try:
        graph = synapse_graph.SynapseGraph(
            name='matrix.opulus.space',
            headers={'Authorization': f'Bearer {settings.MATRIX_TOKEN}'},
            matrix_homeserver='matrix.opulus.space',
            hide_usernames=True,
            u2u_relation=False
        )

        _map = json.loads(graph.json)

        # Clear all unnecessary information
        _map = {
            'nodes': _map['nodes'],
            'edges': _map['edges']
        }

        # Save to DB
        _map = Map.objects.create(map=_map)

    except synapse_graph.SynapseGraphError as e:
        print(f'Some problems with map updating: {e}')
