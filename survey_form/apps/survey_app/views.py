from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    if 'counter' not in request.session:
        request.session['counter']=0
        
    return render(request,'survey/index.html')

def process(request):

    request.session['user_data']=request.POST

    request.session['counter']=request.session['counter']+1

    return redirect('/result')

def result(request):
    
    return render(request,'survey/result.html')