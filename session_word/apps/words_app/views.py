from django.shortcuts import render,redirect

from time import gmtime,strftime,localtime

# Create your views here.
def index(request):
    if 'data' not in request.session:
        request.session['data']=[]

    return render(request,"words/index.html")

def process(request):
    
    date_time={
    'date':strftime("%B %dth, %Y", localtime()),
    'time':strftime("%H:%M:%S%p", localtime())
    }
    if 'fonts' in request.POST:
        showbig = 30
    else:
        showbig = 20

    a_dict={
        'word':request.POST['word'],
        'color':request.POST['color'],
        'fonts':showbig,
        'date':date_time['date'],
        'time':date_time['time']
    }

    temp_list=request.session['data']
    temp_list.append(a_dict)
    request.session['data']=temp_list

    print(request.session['data'])


    return redirect("/")


def delete(request):
    del request.session['data']
    return redirect("/")