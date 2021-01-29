from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='first'),
    path('sign/', views.signPage, name='sign')
]