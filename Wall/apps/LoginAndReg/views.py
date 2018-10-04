from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User
# Create your views here.

def index(request):

    if 'user_id' not in request.session:
        request.session['user_id']=0

    return render(request,'logAndreg/index.html')

    
def create(request):

    valid,response=User.objects.validator(request.POST)

    request.session['tempUserData']={
        'firstname':request.POST['firstname'],
        'lastname':request.POST['lastname'],
        'email':request.POST['email']
    }

    if validateResponse(request,valid,response):
        messages.success(request, "Successfully Registered")
        del request.session['tempUserData']
        return redirect(reverse("wall:index"))
    else:
        return redirect(reverse("userLG:registration"))
    

def login(request):

    return render(request,'logAndreg/login.html')
    
def proccess(request):

    valid,response=User.objects.loginValidation(request.POST)

    if validateResponse(request,valid,response):
        return redirect(reverse("wall:index"))
    else:
        return redirect(reverse("userLG:login"))
    



def validateResponse(request,valid,response):
    if valid==False:
        for error in response:
            messages.error(request, error)
        return False

    else:
        request.session['user_id']=response

        return True