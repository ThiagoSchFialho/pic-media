from django.shortcuts import render

def login(request):
    return render(request, 'users/login.html')

def sign_up(request):
    return render(request, 'users/sign_up.html')