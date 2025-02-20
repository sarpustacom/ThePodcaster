from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.CreateAccountView.as_view(), name="register"),
    path("", views.index, name="index"),
    path("log_out/", views.log_out, name="log_out")
]