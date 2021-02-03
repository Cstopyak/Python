from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
def index(request):
    # del request.session['loginID']
    return render(request, "mainlogin.html")

def register(request):
    print(request.POST)

    ValidationError = User.objects.regValidator(request.POST)
    print("Errors are below.")
    print(ValidationError)

    if len(ValidationError)> 0:
        for key, value in ValidationError.items():
            messages.error(request, value)
        return redirect("/")

    else: 
        newUser = User.objects.create(name = request.POST['name'], username = request.POST['username'], password = request.POST['pass'])

    request.session['loginID'] = newUser.id 

    return redirect("/dashboard")

def dashboard(request):
    if 'loginID' not in request.session:
        messages.error(request, "Please log in.")
        return redirect("/")

    context ={
        'loginUser': User.objects.get (id= request.session['loginID']),
        'AllItems': item.objects.all(),
        'favitem': item.objects.filter(wishlisted = User.objects.get (id= request.session['loginID'])),
        'nonfavitem': item.objects.exclude(wishlisted = User.objects.get (id= request.session['loginID']))

    }


    return render(request, 'dashboard.html', context)


def login(request):
    print(request.POST)
    ValidationError = User.objects.loginValidation(request.POST)
    print("Errors are below.")
    print(ValidationError)

    if len(ValidationError)> 0:
        for key, value in ValidationError.items():
            messages.error(request, value)
        return redirect("/")
    else:
        userswithSameusername = User.objects.filter(username = request.POST['username'])
        request.session['loginID'] = userswithSameusername[0].id

    return redirect("/dashboard")

def logout(request):
    request.session.clear()

    return redirect("/")

def itemcreate(request):
    return render(request, "itemcreate.html")

def uploaditem(request):
    print(request.POST)
    ValidationError = item.objects.createItemVal(request.POST)
    print(ValidationError)

    if len(ValidationError)> 0:
        for key, value in ValidationError.items():
            messages.error(request, value)
        return redirect("/wish_item/create")
    else:
        item.objects.create(item_name = request.POST['item/product'], created_item = User.objects.get (id= request.session['loginID']))

    return redirect("/dashboard")


def ItemInfo(request, ItemId):
    context = {
        'itemselected': item.objects.get(id= ItemId)
    }


    return render(request, "iteminfo.html", context)

def addtofav(request, ItemId):
    item.objects.get(id= ItemId).wishlisted.add(User.objects.get(id= request.session['loginID']))
    
    return redirect("/dashboard")

