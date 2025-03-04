from django.urls import path, include
from . import views

# Handled in views.py, located in the same path where urls.py. views.index - index is a function inside views.py file
urlpatterns = [
    path('debug/', views.debug, name='deb'), # Debug console test. works. Delete
    path('', views.index, name='index'),
]
