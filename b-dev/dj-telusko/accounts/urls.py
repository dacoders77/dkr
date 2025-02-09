from django.urls import path, include
from . import views

# Handled in views.py, located in the same path where urls.py. views.index - index is a function inside views.py file
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]
