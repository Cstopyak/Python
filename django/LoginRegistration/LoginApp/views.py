from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    # del request.session['loginID']
    return render(request, "LoginR.html")

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
        newUser = User.objects.create(fname = request.POST['fname'], lname = request.POST['lname'], email = request.POST['email'], password = request.POST['pass'])

    request.session['loginID'] = newUser.id 

    return redirect("/success")

def success(request):
    if 'loginID' not in request.session:
        messages.error(request, "Please log in.")
        return redirect("/")

    context ={
        'loginUser': User.objects.get (id= request.session['loginID'])
    }


    return render(request, 'success.html', context)


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
        userswithSameEmail = User.objects.filter(email = request.POST['email'])
        request.session['loginID'] = userswithSameEmail[0].id

    return redirect("/success")

def logout(request):
    request.session.clear()

    return redirect("/")