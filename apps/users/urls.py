from django.urls import path
from apps.users.views import login, sign_up

urlpatterns = [
    path('/login', login, name='login'),
    path('/sign_up', sign_up, name='sign_up')
]
