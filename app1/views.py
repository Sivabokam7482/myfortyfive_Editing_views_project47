from django.shortcuts import render
from app1.models import*
from django.views.generic import *
# Create your views here.
class Home(TemplateView):
    template_name='app1/home.html'


class schoollist(ListView):
    model=School
    context_object_name='schools'


class schooldetail(DetailView):
    model=School
    context_object_name='sc'

class schoolcreate(CreateView):
    model=School
    fields='__all__'

class schoolupdate(UpdateView):
    model=School
    fields='__all__'