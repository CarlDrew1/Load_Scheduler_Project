from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View
from django.contrib.auth.forms import UserCreationForm
from .models import Runs
from django.contrib.auth import authenticate, login
from .filters import filter_runs
from .permit import permit_call
from django.utils import timezone
from .utils import render_to_pdf
from django.http import HttpResponse
from django_tables2 import SingleTableView
from .tables import RunTable
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin




def home(request):
    return render(request, 'Runs/home.html')


class SignUp(CreateView):
    form_class= UserCreationForm
    success_url=reverse_lazy('Table_View')
    template_name ='registration/signup.html'

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view


class create_run(CreateView):
    model = Runs
    fields = ['run','driver', 'truck','trailer_1', 'trailer_2', 'load_comments', 'return_load_comments','depart_date','depart_time','Planned_depart_time','foodstuffs', 'gib', 'run_details','weight', 'cubic']
    template_name = 'Runs/create_run.html'
    success_url =   reverse_lazy('Table_View')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(create_run, self).form_valid(form)
        return redirect('Table_View')


class Table_View(SingleTableMixin,FilterView):
    model = Runs
    table_class = RunTable
    template_name = 'Runs/table.html'
    filterset_class = filter_runs

    def get_filterset_kwargs(self,*args):
        kwargs = super().get_filterset_kwargs(*args)
        if kwargs['data']:
            bucket_filter_data = kwargs['data']
            self.request.session['bucket_filter_data']= bucket_filter_data
        else:
            if 'bucket_filter_data' in self.request.session.keys():
                kwargs['data']=self.request.session['bucket_filter_data']
        return kwargs 

    

class detail_run(ListView):
    model = Runs
    runset = Runs.objects.all()
    template_name ='Runs/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = filter_runs(self.request.GET, queryset=self.get_queryset())
        return context
        

class update_run(UpdateView):
    model = Runs
    template_name ='Runs/update.html' 
    fields = ['run','driver', 'truck','trailer_1', 'trailer_2', 'load_comments', 'return_load_comments','depart_date','depart_time','Planned_depart_time','finished_loading_time','foodstuffs', 'gib','run_details','weight', 'cubic']
    success_url =   reverse_lazy('Table_View')

    
class delete_run(DeleteView):
    model = Runs
    template_name ='Runs/delete.html' 
    success_url =   reverse_lazy('Table_View')


class GeneratePdf(DetailView):
    model = Runs
    
   
    def get(self, request, pk, *args, **kwargs):
        runset = Runs.objects.get(pk=self.kwargs.get('pk'))
        data = {
             'runset': runset, 
        }
        pdf = render_to_pdf('Runs/pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
 

    



