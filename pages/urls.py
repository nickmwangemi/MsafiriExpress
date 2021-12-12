from django.urls import include, path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
]
