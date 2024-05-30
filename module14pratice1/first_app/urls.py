from django.urls import path, include
from . import views

urlpatterns = [    
    path('app/', views.add_apps, name='add_apps'),
]
