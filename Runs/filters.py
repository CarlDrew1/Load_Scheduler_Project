import django_filters
from .models import Runs
from django import forms
import datetime
from django.utils import timezone 





class filter_runs(django_filters.FilterSet):
    planning_date = django_filters.DateFilter(
    widget=forms.DateInput(
        attrs={
            'id': 'plan_date',
            'type': 'text',
            'placeholder': 'Planning Date',
            'value': datetime.datetime.now().strftime("%Y-%m-%d"),            
        }))
    class Meta:
        model = Runs
        fields = ['planning_date']