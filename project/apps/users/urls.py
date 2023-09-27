from django.urls import path
from .views import UserDetailAPI, RegisterUserAPIView

urlpatterns = [
  path("me", UserDetailAPI.as_view()),
  path('register', RegisterUserAPIView.as_view()),
]
