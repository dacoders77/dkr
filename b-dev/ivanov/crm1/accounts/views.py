from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * # Import all models
from .forms import OrderForm

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = Customer.objects.count()
    total_orders = Order.objects.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    return render(request, 'accounts/dashboard.html', {'orders':orders, 'customers':customers, 'total_customers':total_customers,
                                                       'total_orders':total_orders, 'delivered':delivered, 'pending':pending})

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products}) # Pass a dict of values to template

def customer(request, pk_test):
    customer = Customer.objects.get(pk=pk_test)
    orders = customer.order_set.all() # Query child objects
    order_count = orders.count()
    context = {'customer': customer, 'orders':orders, 'order_count':order_count}
    return render(request, 'accounts/customer.html', context)

def create_order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(pk=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)



