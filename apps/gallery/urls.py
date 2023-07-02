from django.urls import path
from apps.gallery.views import index, main_gallery
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('/main_gallery', main_gallery, name='main_gallery'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
