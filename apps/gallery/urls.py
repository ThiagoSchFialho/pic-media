from django.urls import path

from apps.gallery.views import index, main_gallery, upload

urlpatterns = [
    path('', index, name='index'),
    path('main_gallery/', main_gallery, name='main_gallery'),
    path('upload/', upload, name='upload'),
]
