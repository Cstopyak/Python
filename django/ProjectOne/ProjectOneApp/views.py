from django.shortcuts import render, HttpResponse,redirect
def index(request):
    return HttpResponse("Hello Project One")

def blogs(request):
    return HttpResponse("This is the blogs area.")

def methods(request):
    return HttpResponse("This is the advance methods")

def showamethod(request, methods):
    return HttpResponse(f"This is method 1, 2, 3: {methods}")

def nopage(request):
    return redirect("/destroy")
