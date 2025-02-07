from django.conf.urls.i18n import urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Handled in views.py
    path('add', views.add, name='add'),
]