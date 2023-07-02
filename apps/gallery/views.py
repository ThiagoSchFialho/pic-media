from django.shortcuts import render, redirect
from apps.gallery.models import Picture

def index(request):
    if request.user.is_authenticated:
        return redirect("main_gallery")
        
    return render(request, 'gallery/index.html')

def main_gallery(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        pass

    pictures = Picture.objects.all()

    return render(request, 'gallery/main_gallery.html', {"pictures": pictures, "user_is_authenticated": True})