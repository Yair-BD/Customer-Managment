from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('product/',products, name='product'),
    path('customer/<str:pk>/',customer, name='customer'),
    path('create_order/<str:pk>/',createorder, name='create_order'),
    path('update_order/<str:pk>/',update_order, name='update_order'),
    path('delete_order/<str:pk>/',delete_order, name='delete_order'),

    path('',home, name='home'),
]