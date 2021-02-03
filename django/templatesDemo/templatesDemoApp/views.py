from django.shortcuts import render, HttpResponse, redirect
from datetime import date

# Create your views here.
def index(request):
    if 'visitcount' not in request.session:
        request.session['visitcount'] = 1
    else:
        request.session['visitcount'] += 1
    
    print(f"printing the request method which is: {request.method}")
   
    allGreatShows = [
        {'id':1, 'title':"Sponge Bob", 'network': "Nick"},
        {'id':2, 'title':"Always Sunny in Philly", 'network': "FX"},
        {'id':3, 'title':"Chappelle Show", 'network': "Comedy Central"},
        {'id':4, 'title':"Cosby Show", 'network': "Nick at Nite"}
    ]
    today = date.today()
    print(today)
    #anything i want to send to HTML, needs to be inside of context
    context = {
        'shows': allGreatShows,
        'todaydate': today
    }

    return render(request, "wazzaa.html", context)

def processForm(request):
    print(f"printing the request method which is: {request.method}")
    #THE INFORMATION FORM THE FORM IS REPRESENTED BY request.POST
    print('request.post in the process form function',request.POST) #request.post is a dictionary that has key value pairs
    print(request.POST['favshow'])
    request.session['forminfo'] = request.POST

    return redirect("/success")

def showResults(request):
    print('request.post in the showResults function',request.POST)
    return render(request,'result.html')


def add100(request):
    print("you clicked to add 100!")
    request.session['visitcount'] += 99
    return redirect('/')
# {'cookie1': 5,
# 'cookie2':"hello",
    # 'forminfo': request.POST
# }

