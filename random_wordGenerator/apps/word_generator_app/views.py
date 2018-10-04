from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):

    random_letters={'random_letters':get_random_string(length=14)}

    if 'counter'  not in request.session:
        request.session['counter']=0

    return render(request,'word_generator/index.html',random_letters)

def process(request):

    request.session['counter']=request.session['counter']+1 
    return redirect("/")

def reset(request):
    del request.session['counter']
    return redirect("/")