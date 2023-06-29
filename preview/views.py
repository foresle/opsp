import json

from django.views.generic import TemplateView

from .models import Phrases


class PreviewView(TemplateView):
    template_name = 'preview/preview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        phrases = Phrases.objects.all()
        context['phrases'] = json.dumps({
            'phrases': [phrase.phrase for phrase in
                        sorted(list(phrases), key=lambda phrase: int(phrase.priority), reverse=True)]
        })

        return context
