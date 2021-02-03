from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(request):
    # ClassName.objects.all() - gets all the records in the table
    print(User.objects.all())
    context = {
        'allUsr': User.objects.all()
    }
    return render(request, "index.html", context)

def createUser(request):
    #redirect on a post request
    print("*"*20)
    print(request.POST)
    print("*"*20)
    # ClassName.objects.create(field1="value for field1", field2="value for field2", etc.)
    User.objects.create(first_name= request.POST['fname'])
    return redirect("/")

def showUser(request, idUser):
    # ClassName.objects.get(id=1) - gets the record in the table with the specified id
    print("specific USER!"*20)
    print(User.objects.get(id=idUser))
    print("specific USER!"*20)
    context = {
        'oneUser': User.objects.get(id=idUser),
        'allItems': Item.objects.all()
    }

    return render(request, "userInfo.html", context )

def favoriteItem(request, idUser):
    print("&&&&&&&&&&&")
    print(f"id of the user who wants item: {idUser}")
    print(request.POST)
    print(f"id of the liked item : {request.POST['selectedItem']}")
    # this_book = Book.objects.get(id=4)	# retrieve an instance of a book
    this_user = User.objects.get(id=idUser)
    # this_publisher = Publisher.objects.get(id=2)	# retrieve an instance of a publisher
    this_item = Item.objects.get(id=request.POST['selectedItem'])

    # # 2 options that do the same thing:
    # this_publisher.books.add(this_book)
    this_item.favoritors.add(this_user)
    print("&&&&&&&&&&&")
    return redirect(f"/users/{idUser}")