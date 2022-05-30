from django.urls import path

from .views import users

urlpatterns = [
    path('', users.UserList.as_view()),
    path('<int:pk>/', users.UserDetail.as_view())
]
