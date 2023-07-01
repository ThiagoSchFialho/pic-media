from django.shortcuts import render

def index(request):
    user_is_authenticated = False

    if request.user.is_authenticated:
        user_is_authenticated = True
        
    return render(request, 'gallery/index.html', {"user_is_authenticated": user_is_authenticated})