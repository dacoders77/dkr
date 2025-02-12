from dataclasses import fields

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * # Import all models
from .forms import *
from django.forms import inlineformset_factory # To use multiple forms in one object
from .filters import OrderFilter


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

    # On search button click
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs


    context = {'customer': customer, 'orders':orders, 'order_count':order_count, 'myFilter':myFilter}
    return render(request, 'accounts/customer.html', context)

def create_order(request, pk):
    # Parent model, child model. Then what fields we allow from child model. Extra - how many rows to show
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=2)
    customer = Customer.objects.get(pk=pk) # Get the customer using passes id from the form
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
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

# Test form. Delete
def Demoview(request):
    if request.method == 'POST':
        form = DemoForm(request.POST)  # Bind the form to POST data
        if form.is_valid():  # Validate the form
            form.save()  # Save the data to the database
            return redirect('/')  # Redirect to a success page
    else:
        form = DemoForm()  # Create an empty form for GET requests

    context = {'form': form}
    return render(request, 'accounts/test_form.html', context)

    #return render(request, 'accounts/test_form.html')



