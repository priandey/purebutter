from django.urls import path
from . import views

urlpatterns = [
    path('add_fav/', views.add_favorite, name="add_favorite"),
]