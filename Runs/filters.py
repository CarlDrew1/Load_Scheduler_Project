import django_filters
from .models import Runs
from django import forms





class filter_runs(django_filters.FilterSet):
    depart_date = django_filters.DateFilter(
    
    widget=forms.DateInput(
        attrs={
            'id': 'date',
            'type': 'text',
            'place holder': 'Depart Date',
        }
    )
    )

    class Meta:
        model = Runs
        fields = ['depart_date']