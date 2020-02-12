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



def home(request):
    return render(request, 'Runs/home.html')


class SignUp(CreateView):
    form_class= UserCreationForm
    success_url=reverse_lazy('detail_run')
    template_name ='registration/signup.html'

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view


class create_run(CreateView):
    model = Runs
    fields = ['run','driver', 'truck','trailer_1', 'trailer_2', 'load_comments', 'return_load_comments','depart_date','depart_time','Planned_depart_time']
    template_name = 'Runs/create_run.html'
    success_url =   reverse_lazy('detail_run')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(create_run, self).form_valid(form)
        return redirect('detail_run')
    

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
    fields = ['run','driver', 'truck','trailer_1', 'trailer_2', 'load_comments', 'return_load_comments','depart_date','depart_time','Planned_depart_time','finished_loading_time']
    success_url =   reverse_lazy('detail_run')

    
class delete_run(DeleteView):
    model = Runs
    template_name ='Runs/delete.html' 
    success_url =   reverse_lazy('detail_run')


class GeneratePdf(DetailView):
    model = Runs
    
   
    def get(self, request, pk, *args, **kwargs):
        runset = Runs.objects.get(pk=self.kwargs.get('pk'))
        data = {
             'runset': runset, 
        }
        pdf = render_to_pdf('Runs/pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
 




