from django.conf.urls.i18n import urlpatterns
from django.urls import path
from . import views

# This file is copied from calc dir

urlpatterns = [
    path('', views.index, name='index') # Handled in views.py, located in the same path where urls.py
]