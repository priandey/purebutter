from django.urls import path
from . import views

urlpatterns = [
    path('search', views.search_product, name="search"),
    path('product/<int:id>', views.product, name='product'),
]