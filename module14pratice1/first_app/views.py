from django.shortcuts import render
from . forms import ContactForm
from . import models

# Create your views here.
# def add_apps(request):
#     apps_form = forms.FirstAppForm()
#     return render(request, 'firstapp.html', {'form' : apps_form})


def add_apps(request):
    form = ContactForm()         
    return render(request, 'firstapp.html', {'form' : form})

