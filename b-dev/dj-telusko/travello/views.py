from http.client import responses
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Called from urls 

def index(request):

    destinations = Destination.objects.all()

    #return HttpResponse("<h1>Hello, world. You're at the polls home view.</h1>")
    return render(request, "index.html", {"dests": destinations}) # Index.html is in templates/. Passing a test array

# Test debug method to see ip for django debug console
def debug(request):
    print("travello/views.py internal ip for debug console: " + request.META['REMOTE_ADDR']) # See the ip address on which docker runs the server
    return render(request, "debug.html")
