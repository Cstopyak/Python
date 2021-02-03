from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('AddDojo', views.AddDojo),
    path('AddNinja', views.AddNinja)
]