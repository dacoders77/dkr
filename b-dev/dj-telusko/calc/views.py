from http.client import responses
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Called from calc/urls.py
def home(request):
    #return HttpResponse("<h1>Hello, world. You're at the polls home view.</h1>")
    return render(request, "home.html", {"name":"boris"})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    result = val1 + val2
    return render(request, "result.html", {"result":result})
