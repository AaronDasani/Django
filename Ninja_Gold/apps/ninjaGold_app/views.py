from django.shortcuts import render,redirect

import random
import datetime
import time
# Create your views here.
def index(request):
    if 'total' not in request.session:
        request.session['total']=0
    if 'history' not in request.session:
        request.session['history']=[]
    return render (request,'ninjaGold/index.html')





def process(request,number):

    number=int(number)

    
    the_time=datetime.datetime.now().strftime("20%y/%m/%d %I:%M %p")
    location_map = {
        'farm': random.randint(10, 20),
        'cave': random.randint(5,10),
        'house': random.randint(2,5),
        'casino': random.randint(-50,50),
    }
    if request.POST['location'] not in location_map:
        print('Location doesnt exist')
        return redirect('/')

    gold=location_map[request.POST['location']]

    request.session['total'] += gold

    a_dict={
            'location':request.POST['location'],
            'gold':gold,
            'time':the_time
        }
        
    request.session['history'].append(a_dict)
    return redirect ('/')
   