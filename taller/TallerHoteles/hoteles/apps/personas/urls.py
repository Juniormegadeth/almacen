from django.urls import path
from apps.personas.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]
