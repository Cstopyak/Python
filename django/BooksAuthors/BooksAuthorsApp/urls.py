from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('books/<int:idBook>', views.books),
    path('AddAuthor/<int:idauthor>', views.AddAuthor),	   
]