from django.shortcuts import render,redirect

from time import gmtime,strftime,localtime,time

# Create your views here.
def index(request):

    date_time={
        'date':strftime("%b %d, %Y", localtime()),
        'time':strftime("%H:%M %p", localtime())
    }

    print(date_time['date'])

    return render(request,'TimeAndDate/index.html',date_time)