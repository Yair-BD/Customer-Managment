from django.contrib import admin
from django.urls import path
from .views import home, customer, products

urlpatterns = [
    path('product/',products),
    path('customer/',customer),
    path('',home),
]