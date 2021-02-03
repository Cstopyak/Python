from django.shortcuts import render, HttpResponse 
import datetime
from datetime import date, datetime

    
def index(request):
    today = date.today()
    time = datetime.now()
    context = {
        'todaydate' : today,
        'datetime' : time
    }

    
    return render(request,'index.html', context)
    