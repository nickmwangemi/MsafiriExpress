from django.urls import include, path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path("daraja/stk-push", views.stk_push_callback, name="mpesa_stk_push_callback")
]
