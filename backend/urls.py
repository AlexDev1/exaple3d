"""
URL configuration for backend project.
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import get_scene

urlpatterns = [
    path("api/project/<int:project_id>/scene/", get_scene, name="get_scene"),
]

# Добавляем обслуживание статических файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]) 