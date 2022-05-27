from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UserDetail.as_view())
]
