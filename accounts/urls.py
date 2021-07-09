from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('product/',products, name='product'),
    path('customer/<str:pk>/',customer, name='customer'),
    path('create_order/',createorder, name='create_order'),
    path('',home, name='home'),
]