from django.shortcuts import render


def home(request):
    return render(request, 'accounts/dashboad.html')

def product(request):
    return render(request, 'accounts/product.html')

def customer(request):
    return render(request, 'accounts/customer.html')