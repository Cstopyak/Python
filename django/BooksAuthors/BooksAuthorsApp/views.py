from django.shortcuts import render, HttpResponse, redirect
from .models import *



def index(request):

    context={
        'AllBks': Book.objects.all()
    }
    return render(request, 'index.html', context)

def books(request, idBook):
    context={
        'id': Book.objects.get(id= idBook),
        'desc': Book.objects.all(),
        'AllAuthors': Author.objects.all()
    }
    return render(request, "books.html", context)

def AddAuthor(request, idauthor):
    print("New Author Submitted Successfully")
    print(request.POST)
    this_Book= Book.objects.get(id=idauthor)
    
    this_author = Author.objects.get(id=request.POST['AddAuthor'])

    this_Book.authors.add(this_author)
    return redirect("/books/" + str(idauthor))