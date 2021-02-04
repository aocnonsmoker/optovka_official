from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopPage, name='shop'),
    path('c/<slug:slug>/', views.brand_list, name='brands'),
    path('p/<slug:slug>/', views.products_list, name='products'),
    path('d/<int:id>/', views.product_detail, name='detail'),
]