from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages


def register2(request):
    print("Req method:", request.method)
    if request.method == "POST":
        print("POST data:", request.POST.dict())  # Debugging: Print form data
        return JsonResponse({"message": "Received POST request successfully!"})  # Temporary response
    return render(request, "register.html")  # Return the form on GET requests


def register(request):

    if request.method == "POST":
        #first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password1']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("User with that username already exists")
                messages.info(request, "Username already taken!")
                return redirect("register") # Return to the register page if reg failed
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken!")
                return redirect("register")
            else:
                user = User.objects.create_user(first_name="d", last_name=last_name, username=username,
                                                password=password1, email=email)
                user.save()
                messages.success(request, "User created successfully!")
                return redirect("login")

        else:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        return redirect("/")
    else:
        return render(request, "register.html")



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/") # Return to home page
        else:
            messages.error(request, "Invalid username or password!")
            return redirect("login")

    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect("/") # Go back to home page


