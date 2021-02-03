from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("submitShow", views.processForm),
    path("success", views.showResults),
    path("addhundred", views.add100)
]

