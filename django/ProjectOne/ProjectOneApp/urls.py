from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('blogs', views.blogs),
    path('blogs/methods', views.methods),
    path('blogs/methods/<int:methods>', views.showamethod),
    path("destroy", views.nopage)
]