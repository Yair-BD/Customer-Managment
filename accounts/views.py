from django.shortcuts import render, redirect
from .models import *
from .form import OrderForm


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

def customer(request, pk):
    customers = Customer.objects.get(id=pk)
    orders_customer = customers.order_set.all() # זה נותן לי את כל ההזמנות במקושרות את לקוח אחד . 
    total_orders = orders_customer.count()
    context = {"customers": customers, "orders": orders_customer, "total_orders": total_orders}
    return render(request, 'accounts/customer.html', context)

def createorder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {"form": form}
    return render(request, 'accounts/create_order.html', context)


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance= order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {"form": form, "order":order}
    return render(request, 'accounts/create_order.html', context)

def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {"order":order}
    return render(request, 'accounts/delete_order.html', context)