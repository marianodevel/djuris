from django.views.generic import DetailView, ListView

from .models import Causa


class CausaListView(ListView):
    model = Causa


class CausaDetailView(DetailView):
    model = Causa
