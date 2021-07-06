from django.shortcuts import render
from .models import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers =Customer.objects.all().count()
    total_orders =Order.objects.all().count()
    delivered = Order.objects.filter(status="Delivered").count()
    pending = Order.objects.filter(status="Pending").count()
    context = {"orders": orders, "customers": customers, "total_customers": total_customers,
     "total_orders": total_orders, "delivered": delivered, "pending": pending }
    return render(request, 'accounts/dashboad.html', context)

def products(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'accounts/product.html', context)

def customer(request):
    return render(request, 'accounts/customer.html')