from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        return redirect("gallery")
        
    return render(request, 'gallery/index.html')

def gallery(request):
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request, 'gallery/gallery.html', {"user_is_authenticated": True})