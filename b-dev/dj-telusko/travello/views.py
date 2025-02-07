from http.client import responses
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

# Called from calc/urls.py
def index(request):

    dest = Destination()
    dest.name = "Moscow"
    dest.desc = "desc"


    #return HttpResponse("<h1>Hello, world. You're at the polls home view.</h1>")
    return render(request, "index.html", {"dest1": dest})
