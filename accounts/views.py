from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import *
from .form import OrderForm, CreateUserForm
from .filter import OrderFilter
from django.contrib import messages

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers =Customer.objects.all().count() # מיבא את הסכום של כל המופעים
    total_orders =Order.objects.all().count()
    delivered = Order.objects.filter(status="Delivered").count() # סכום של מופעים עם סטטוס מסויים
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

    my_filter = OrderFilter(request.GET, queryset=orders_customer) # מגניס את כל החיפוש שלי תחת הקוח שאני בדף שלו
    orders_customer = my_filter.qs

    context = {"customers": customers, "orders": orders_customer, "filter": my_filter, "total_orders": total_orders}
    return render(request, 'accounts/customer.html', context)

def createorder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status', 'note'), extra=10 ) # (מספר שורות שאני רוצה שיציגו לי איזה שדות אני רוצה לשחק איתם, ילד , הורה)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none() ,instance=customer) #(איזה לקוח ספציפי אני רוצה, וזה שאני לא רוצה שום דבר מהברירות מחדל שלו )
    #form = OrderForm(initial={"customer":customer}) # לגבי אובייקט מסויים שאני רוה שיהיה לו ערך התחלתי 
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {"formset": formset}
    return render(request, 'accounts/create_order.html', context)


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
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

def user_page(request):
    return render(request, 'accouns/user.html')

def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid :
            form.save()
            name = form.cleaned_data.get('username') # מושכים מהנתונים את הצורה הנקייה של נטו השם משתמש שהרגע נרשם לנו 
            messages.success(request, f"Account was created for: {name}")
            return redirect('login-page')

    context = {"form": form}
    return render(request, 'accounts/register.html', context) 
    
def login_page(request):
    context = {}
    return render(request, 'accounts/login.html', context)