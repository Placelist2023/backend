from django.urls import path
from .views import UserDetailAPI, RegisterUserAPIView, update_user_info

urlpatterns = [
  path("me", UserDetailAPI.as_view()),
  path("<pk>", update_user_info),
  path('register', RegisterUserAPIView.as_view()),
]
