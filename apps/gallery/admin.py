from django.contrib import admin
from apps.gallery.models import Picture

class PictureList(admin.ModelAdmin):
    list_display = ("name", "author")
    list_filter = ("author",)
    list_per_page = 30

admin.site.register(Picture, PictureList);