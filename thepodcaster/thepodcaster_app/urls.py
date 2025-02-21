from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    #path("register/", views.CreateAccountView.as_view(), name="register"),
    path("", views.index, name="index"),
    path("log_out/", views.log_out, name="log_out"),
    path("dashboard/shows/", views.shows, name="shows"),
    path("dashboard/episodes/", views.episodes, name="episodes"),
    path("dashboard/shows/add", views.add_show, name="add_show"),
    path("shows/rss/<int:id>/", views.get_rss, name="get_rss")
]