import random

from django.views.generic import TemplateView

from tips.models import Tip


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tips = Tip.objects.all()
        if len(tips) != 0:
            tip = random.choice(tips)
            context['tip'] = tip
        else:
            context['tip'] = None
        return context
