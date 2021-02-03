from django.shortcuts import render, HttpResponse, redirect
from .models import Model_orm

def index(request):
    print(Model_orm.objects.all())
    context = {
        'allModel': Model_orm.objects.all()
    }


    return render(request,"index.html", context)

def newuser(request):
    print("success!")
    print(request.POST)
    createuser = Model_orm.objects.create(fname= request.POST['fname'], lname= request.POST['lname'],email= request.POST['email'], age= request.POST['age'] )
    return redirect(f"/User/{createuser.id}")

def Usernew(request):
    return render(request,"newUser.html")

def Userinfo(request, UserID):
    context ={
        'UserInf': Model_orm.objects.get(id=UserID)
    }

    return render(request, 'info.html', context)

def deleteUser(request, UserID):
    
    userdelete= Model_orm.objects.get(id=UserID)
    userdelete.delete()
    return redirect("/User")

def editUser(request, UserID):
    context ={
        'UserInf': Model_orm.objects.get(id=UserID)
    }
    
    return render(request, 'edit.html', context)

def updateUser(request, UserID):

    userupdate= Model_orm.objects.get(id=UserID)
    userupdate.fname = request.POST['fname']
    userupdate.lname = request.POST['lname']
    userupdate.email = request.POST['email']
    userupdate.age = request.POST['age']
    userupdate.save()

    return redirect(f"/User/{UserID}")