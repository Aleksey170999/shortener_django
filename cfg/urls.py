from django.contrib import admin
from django.urls import path, include

from shortener.api.views import ShortUrls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shortener.api.urls')),
    path('<str:code>/', ShortUrls.as_view({'get': 'retrieve'})),
]

