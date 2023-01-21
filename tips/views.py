from django.views.generic import DetailView, ListView

from .models import Tip


class TipDetailView(DetailView):
    model = Tip


class TipListView(ListView):
    model = Tip
    paginate_by = 10
