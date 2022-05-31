from django.urls import path

from .views import auth

urlpatterns = [
    path('signin/', auth.signin),
    path('signout/', auth.sign_out)
]
