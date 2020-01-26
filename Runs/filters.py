import django_filters
from .models import Runs
from django import forms





class filter_runs(django_filters.FilterSet):
    depart_date = django_filters.DateFilter(
    lookup_expr='icontains',
    widget=forms.DateInput(
        attrs={
            'id': 'date',
            'type': 'text'
        }
    )
    )

    class Meta:
        model = Runs
        fields = ['depart_date']