from django.urls import path
from apps.gallery.views import index

urlpatterns = [
    path('', index, name='index'),
]
