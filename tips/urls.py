from django.urls import path
from .views import TipDetailView, TipListView

urlpatterns = [
    path('<int:pk>/', TipDetailView.as_view(), name='tip_detail'),
    path('', TipListView.as_view(), name='tip_list'),
]
