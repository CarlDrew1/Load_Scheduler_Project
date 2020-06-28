import django_tables2 as tables
from .models import Runs
from django_tables2.utils import A

class RunTable(tables.Table):
    depart_date = tables.DateColumn(format= 'd/m/Y')
    planning_date = tables.DateColumn(format= 'd/m/Y')
    Update =tables.LinkColumn('update_run', text='➡', args=[A('pk')], \
                         orderable=False, empty_values=(), exclude_from_export=True)
    Print =tables.LinkColumn('GeneratePdf', text='🖨', args=[A('pk')], \
                         orderable=False, empty_values=(), exclude_from_export=True)
    Delete =tables.LinkColumn('delete_run', text='❌', args=[A('pk')], \
                         orderable=False, empty_values=(), exclude_from_export=True)
    export_formats = ['csv']
    

    class Meta:
        model = Runs
        # template_name = "django_tables2/bootstrap4.html"
        fields = ("run","run_details", "planning_date", "depart_date", "Planned_depart_time", "driver", "truck", "trailer_1", "trailer_2", "Unit_Permitted","foodstuffs", "gib", "load_comments", "return_load_comments" ,'weight', 'cubic' )

    