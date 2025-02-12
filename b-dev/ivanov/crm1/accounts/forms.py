from django.forms import ModelForm
from .models import Order, DemoClass # Create models first to use them in forms
from django import forms


class OrderForm(ModelForm):
    class Meta:
        model = Order # Use the model we created in models.py
        fields = '__all__'


class DemoForm(ModelForm):
    class Meta:
        model = DemoClass # Use the model
        fields = "__all__"
        widgets = {
            'field1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Field1'}),
            'field2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Field2'}),
            'field3': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Field3'}),
            'field4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Field4'}),
        }