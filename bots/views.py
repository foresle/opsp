from django.views.generic import ListView, DetailView

from .models import Bot


class BotListView(ListView):
    model = Bot
    paginate_by = 3


class BotDetailView(DetailView):
    model = Bot
