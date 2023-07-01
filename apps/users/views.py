from django.shortcuts import render
from apps.users.forms import LoginForm

def login(request):
    form = LoginForm()
    return render(request, 'users/login.html', {"form": form})

def sign_up(request):
    return render(request, 'users/sign_up.html')