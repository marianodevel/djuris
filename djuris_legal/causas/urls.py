from django.urls import path

from .views import CausaDetailView, CausaListView

urlpatterns = [
    path("", CausaListView.as_view(), name="causas"),
    path("causa/<int:pk>/", CausaDetailView.as_view(), name="detalle_causa"),
]
