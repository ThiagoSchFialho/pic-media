from django.shortcuts import render
from apps.users.forms import LoginForm, SignUpForm

def login(request):
    form = LoginForm()
    return render(request, 'users/login.html', {"form": form})

def sign_up(request):
    form = SignUpForm()
    return render(request, 'users/sign_up.html', {"form": form})