from django.shortcuts import render
from django.http import HttpResponse
from .models import * # Import all models


# Create your views here.

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

def customer(request):
    return render(request, 'accounts/customer.html')

