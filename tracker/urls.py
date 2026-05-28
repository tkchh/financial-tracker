from django.urls import path

from tracker.views import (
    HomeView,
    SignUpView,
    UserLoginView,
    UserLogoutView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]