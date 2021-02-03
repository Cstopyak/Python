from django.urls import path     
from .import views
urlpatterns = [
    path('', views.index),
    path("register", views.register),
    path("dashboard", views.dashboard),
    path("wish_item/create", views.itemcreate),
    path("uploaditem", views.uploaditem),
    path("logout", views.logout),
    path("login", views.login),
    path("dashboard/<int:ItemId>", views.ItemInfo),
    path("addtofav/<int:ItemId>", views.addtofav),
]