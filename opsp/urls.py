from django.contrib import admin
from django.urls import path, include

from home.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('map/', include('map.urls')),
    path('bots/', include('bots.urls')),
    path('tips/', include('tips.urls')),
    path('', HomeView.as_view(), name='home'),
]
