from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Dojo, Ninja
def index(request):
    print(Dojo.objects.all())
    context = {
        'AllInfo': Dojo.objects.all()
    }
    return render(request, "index.html", context)

def AddDojo(request):
    print("Dojo Submitted Successfully")

    Dojo.objects.create(name=request.POST['nameinput'], city = request.POST['cityinput'], state = request.POST['stateinput'])
    return redirect("/")

def AddNinja(request):
    print("New Ninja Submitted Successfully")
    print(request.POST)
# Ninja.objects.create(fname = "Whitney", lname = "xyz", dojo = Dojo.objects.get(id=7))
    Ninja.objects.create(fname=request.POST['fnameinput'], lname = request.POST['lnameinput'], dojo = Dojo.objects.get(id=request.POST['dojoinput']))
    return redirect("/")