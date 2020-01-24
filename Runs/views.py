from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .models import Runs
from django.contrib.auth import authenticate, login



def home(request):
    return render(request, 'Runs/delete.html')


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
    fields = ['run','driver', 'truck','trailer_1', 'trailer_2', 'load_comments', 'return_load_comments','depart_date','depart_time']
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

class update_run(UpdateView):
    model = Runs
    template_name ='Runs/update.html' 
    fields = ['run','driver', 'truck','trailer_1', 'trailer_2', 'load_comments', 'return_load_comments','depart_date','depart_time']
    success_url =   reverse_lazy('detail_run')

    
class delete_run(DeleteView):
    model = Runs
    template_name ='Runs/delete.html' 
    success_url =   reverse_lazy('detail_run')

