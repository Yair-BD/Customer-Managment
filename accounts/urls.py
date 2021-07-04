from django.contrib import admin
from django.urls import path
from .views import home, customer, product

urlpatterns = [
    path('product/',product),
    path('customer/',customer),
    path('',home),
]