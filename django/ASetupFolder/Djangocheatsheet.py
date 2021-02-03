Create your environment AND installation

------------------------------------------------------------------
| Mac/Linux: | python3 -m venv djangoPy3Env 

Activate your environment:

------------------------------------------------------------------
| Mac/Linux: | source djangoPy3Env/bin/activate 


Install Django:

(djangoPy3Env) Windows/Mac:| pip install Django==2.2.4

creating a Project

> cd python_stack/django/django_intro
django_intro> django-admin startproject your_project_name_here


django_intro> cd your_project_name_here
your_project_name_here> python manage.py runserver
open local host8000

hit CTRL C

your_project_name_here> python manage.py startapp your_app_name_here

next**

your_project_name_here/your_project_name_here/settings.py

Add app name into settings.py

next add code below your_project_name_here/your_project_name_here/urls.py
from django.urls import path, include           # import include
# from django.contrib import admin              # comment out, or just delete
urlpatterns = [
    path('', include('your_app_name_here.urls')),	   
    # path('admin/', admin.sites.urls)         # comment out, or just dele

now in your App folder add a file urls.py

add this:

from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),  
]
** make sure there is no space when coping it can be invisible after views.index), on line 50

finally

go to views.py in you app folder

from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

    python manage.py runserver

    you should see this phrase in localhost:8000

    this is the equivalent of @app.route('/')!
