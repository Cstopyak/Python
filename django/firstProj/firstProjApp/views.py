from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import User, Post


#all our functions are going to be in this views.py file
def index(request):
    # print(User.objects.all())
    context = {
        'allUsers': User.objects.all()
    }
    return render(request, "usersPosts.html", context)

def createUser(request):
    #on a post request-> redirect to a different url
    print("submitted post request")
    # print(request.POST)
    # ClassName.objects.create(field1="value for field1", field2="value for field2", etc.)
    User.objects.create(first_name=request.POST['fname'], last_name = request.POST['lname'], age = request.POST['ageInput'])
    return redirect("/")


def createPost(request):
    print("*" * 10)
    print(request.POST)
    print("*" * 10)
    Post.objects.create(content = request.POST['msg'], creator= User.objects.get(id=request.POST['usr']))
    # Post.objects.create(content = "that vegan moonshine though", creator = User.objects.get(id=1))
    return redirect("/")



