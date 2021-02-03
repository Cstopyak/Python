from django.shortcuts import render, HttpResponse, redirect
from random import randint


def index(request):
    if "num" not in request.session:
        request.session["num"] = randint(0, 100)
    return render(request,"index.html")

def guess(request):
    print(request.POST)
    guess= int(request.POST["guess"])

    if guess == request.session["num"]:
        print("right on!")
        request.session["status"] = "correct"
    elif guess > request.session["num"]:
        print("too high")
        request.session["status"] = "too high"    
    else:
        print("way off your cold!!")
        request.session["status"] = "way off your cold"
    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")