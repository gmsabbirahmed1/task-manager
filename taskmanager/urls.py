"""taskmanager URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('tasks.auth_urls')),
    path('', include('tasks.urls')),
]
