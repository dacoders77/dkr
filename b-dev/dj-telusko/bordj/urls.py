"""
URL configuration for bordj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


# Define a simple Hello World view
def hello_world(request):
    return HttpResponse("Hello, World!")

urlpatterns = [
    path('admin/', admin.site.urls), # Default admin page

    path('', include('travello.urls')) # simialr to /travello/urls.py
    #path('', hello_world) # test. hellow_world - passing a function itself, it will be called when a request is made. The function will not be called right away
]
