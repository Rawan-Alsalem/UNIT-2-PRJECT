from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("heritage/", views.heritage_view, name="heritage_view"),
    path("art/", views.art_view, name="art_view"),
    path("architecture/", views.architecture_view, name="architecture_view"),
    path("festivals/", views.festivals_view, name="festivals_view"),
    path("fashion/", views.fashion_view, name="fashion_view"),
    path("music/", views.music_view, name="music_view"),
    path('toggle-font/', views.toggle_font, name='toggle_font'),
]