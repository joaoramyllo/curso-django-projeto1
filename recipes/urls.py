from django.urls import path

from . import views  # mesma coisa que from recipes import views

urlpatterns = [
    path("", views.home),
    path("recipes/<int:id>/", views.recipes),
]
