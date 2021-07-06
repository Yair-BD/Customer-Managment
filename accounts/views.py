from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, 'accounts/dashboad.html')

def products(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'accounts/product.html', context)

def customer(request):
    return render(request, 'accounts/customer.html')