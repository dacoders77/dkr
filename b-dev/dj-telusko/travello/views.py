from http.client import responses
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Called from urls 

def index(request):
    dest = Destination() # Object from models.py
    dest.name = "Moscow"
    dest.desc = "desc"

    arr = {"a":"2", "b":"3", "c":"88"}

    #return HttpResponse("<h1>Hello, world. You're at the polls home view.</h1>")
    return render(request, "index.html", {"name": arr}) # Index.html is in templates/. Passing a test array 

def debug(request):
    print(request.META['REMOTE_ADDR']) # See the ip address on which docker runs the server 
    return render(request, "debug.html")
