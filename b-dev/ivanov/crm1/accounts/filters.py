import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

# Filter based around the model

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte') # Daterange filter
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')
    notes = CharFilter(field_name='notes', lookup_expr='icontains') # Ignore case sensetivity
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']
