import django_filters
from .models import Runs
from django import forms
import datetime
from django.utils import timezone 





class filter_runs(django_filters.FilterSet):
    depart_date = django_filters.DateFilter(
    
    widget=forms.DateInput(
        attrs={
            'id': 'date',
            'type': 'text',
            'placeholder': 'Depart Date',
            'value': datetime.datetime.now().strftime("%Y-%m-%d"),
            
        }
    )
    )

    class Meta:
        model = Runs
        fields = ['depart_date']