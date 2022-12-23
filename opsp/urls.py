from django.contrib import admin
from django.urls import path, include

from home.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', include('map.urls')),
    path('', HomeView.as_view(), name='home'),
]
