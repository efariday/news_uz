from django.urls import path
from users.api_endpoints import (
    RegisterUserAPIView,
    RegisterConfirmAPIView,
    LoginSessionAPIView,
    LogoutSessionAPIView,
    ProfileView,
)

urlpatterns = [
    path("auth/register/", RegisterUserAPIView.as_view(), name="register"),
    path("auth/confirm/", RegisterConfirmAPIView.as_view(), name="confirm"),
    path("auth/login/", LoginSessionAPIView.as_view(), name="login"),
    path("auth/logout/", LogoutSessionAPIView.as_view(), name="logout"),
    path("auth/profile/", ProfileView.as_view(), name="profile"),
]
