from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),

    path("register/", views.CreateAccountView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("log_out/", views.log_out, name="log_out"),

    path("dashboard/shows/", views.shows, name="shows"),
    path("dashboard/episodes/", views.episodes, name="episodes"),

    path("dashboard/shows/add", views.add_show, name="add_show"),
    path("dashboard/episodes/add", views.add_episode, name="add_episode"),

    path("shows/rss/<int:id>/", views.get_rss, name="get_rss"),

    path("dashboard/shows/<int:id>/edit", views.edit_show, name="edit_show"),
    path("dashboard/episodes/<int:id>/edit", views.edit_episode, name="edit_episodes"),

    path("dashboard/options/", views.options, name="options"),

    path("dashboard/shows/delete/<int:id>", views.delete_confirm_show, name="delete_confirm_show"),
    path("dashboard/episodes/delete/<int:id>", views.delete_confirm_episode, name="delete_confirm_episode"),
]