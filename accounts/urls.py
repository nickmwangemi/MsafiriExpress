from django.urls import include, path

from . import views

app_name = "accounts"

urlpatterns = [
    path("login", views.login, name="login"),
    path("loginmodal/<int:pk>", views.loginmodal, name="loginmodal"),
    path("register", views.register, name="register"),
    path("registermodal/<int:pk>", views.registermodal, name="registermodal"),
    path("logout", views.logout, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
]
