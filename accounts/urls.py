from django.contrib import admin
from django.urls import path
from .views import home, customer, products

urlpatterns = [
    path('product/',products, name='product'),
    path('customer/<str:pk>/',customer, name='customer'),
    path('',home, name='home'),
]