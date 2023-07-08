from django.shortcuts import render, redirect
from apps.gallery.models import Picture
from apps.gallery.forms import PictureForm

def index(request):
    if request.user.is_authenticated:
        return redirect("main_gallery")
        
    return render(request, 'gallery/index.html')

def main_gallery(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    pictures = Picture.objects.all()

    return render(request, 'gallery/main_gallery.html', {"pictures": pictures, "user_is_authenticated": True})

def upload(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    form = PictureForm()
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("main_gallery")

    return render(request, 'gallery/upload.html', {"form": form, "user_is_authenticated": True})