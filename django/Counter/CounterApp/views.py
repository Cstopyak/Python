from django.shortcuts import render, HttpResponse, redirect
def index(request):
    if 'visitcount' not in request.session:
        request.session['visitcount'] = 1
    else:
        request.session ['visitcount'] += 1
    return render(request, 'index.html')


def addtwo(request):
    
    request.session['visitcount'] += 1
    return redirect('/')

def reset(request):
    
    request.session['visitcount'] = 0
    return redirect('/')