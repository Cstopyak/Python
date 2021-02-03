
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("createUser", views.createUser),
    path('users/<int:idUser>', views.showUser),
    path('favoriteItem/<int:idUser>', views.favoriteItem)
]
