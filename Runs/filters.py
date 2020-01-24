import django_filters
from .models import Runs




class filter_runs(django_filters.FilterSet):
    class Meta:
        model = Runs
        fields = ['depart_date']