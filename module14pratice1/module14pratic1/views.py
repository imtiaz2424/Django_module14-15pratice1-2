from django.shortcuts import render
from first_app.models import FirstApp

def home(request):
    first_apps = FirstApp.objects.all()
    return render(request, 'home.html', {'data' : first_apps} )

