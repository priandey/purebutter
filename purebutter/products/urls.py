from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>', views.product_detail, name="product_detail"),
    path('search', views.search_product, name="search"),
]