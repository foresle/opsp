from django.urls import path
from .views import BotListView, BotDetailView

urlpatterns = [
    path('<int:pk>/', BotDetailView.as_view(), name='bot_detail'),
    path('', BotListView.as_view(), name='bot_list'),
]
