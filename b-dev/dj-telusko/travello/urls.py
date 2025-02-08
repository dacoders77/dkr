from django.conf.urls.i18n import urlpatterns
from django.urls import path, include
from . import views

import debug_toolbar


# Handled in views.py, located in the same path where urls.py. views.index - index is a function inside views.py file
urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('debug/', views.debug, name='deb'), # Debug console test. works
    path('', views.index, name='index'),
]
