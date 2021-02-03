from django.urls import path     
from . import views
urlpatterns = [
    path('User', views.index),
    path('new', views.newuser),	 
    path("User/new", views.Usernew),
    path("User/<int:UserID>", views.Userinfo),
    path("delete/<int:UserID>", views.deleteUser),
    path("User/<int:UserID>/edit", views.editUser),
    path("User/<int:UserID>/update", views.updateUser)
]