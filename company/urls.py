from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name='company'),
    path('orders/', views.ordersPage, name='orders'),
    path('products/', views.productsPage, name='products'),
    path('staff/', views.staffPage, name='staff'),
    path('stat/', views.statPage, name='stat')
]