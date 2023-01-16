from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView


def home(request):
    return render(request, 'home.html')

def acerca(request):
    return render(request, 'acerca.html')

def mision_vision(request):
    return render(request, 'm&v.html')

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')

def panel(request):
    return render(request, 'panel.html')

