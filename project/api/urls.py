from django.contrib import admin
from django.urls import path, include
from .views import health_check
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('auth/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("admin/", admin.site.urls),
    path("health-check", health_check),
    path("users/", include('apps.users.urls'))
]
