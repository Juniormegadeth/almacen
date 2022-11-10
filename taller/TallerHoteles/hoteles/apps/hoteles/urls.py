from django.urls import path
from apps.hoteles.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]
