from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User
# Create your views here.

def home(request):

    return render(request,'logAndreg/home.html')

def register(request):

    return render(request,'logAndreg/register.html')

    
def create(request):

    valid,response=User.objects.validator(request.POST)

    request.session['tempUserData']={
        'firstname':request.POST['firstname'],
        'lastname':request.POST['lastname'],
        'email':request.POST['email']
    }

    if validateResponse(request,valid,response):
        del request.session['tempUserData']
        # As we are using the same create function, we check if the user is an Admin, if yes, this mean that the user is being created by the Admin....
        if 'user_id' in request.session:
            if User.objects.get(id=request.session['user_id']).user_level==1:
                print("this is the Admin<<<<<----------")
                return redirect(reverse("dashboard:addUser"))

        # if the above if statement is false, this mean that the user being created is a new user
        print("User registration<<<<<<<<<-------------")
        request.session['user_id']=response
        messages.success(request, "Successfully Registered")
        return redirect(reverse("dashboard:Dashboard"))
    else:
        return redirect(reverse("userLG:registration"))
    

def login(request):

    return render(request,'logAndreg/login.html')
    
def proccess(request):

    valid,response=User.objects.loginValidation(request.POST)

    if validateResponse(request,valid,response):
        request.session['user_id']=response
        return redirect(reverse("dashboard:Dashboard"))
    else:
        return redirect(reverse("userLG:login"))
    
def logoff(request):
    del request.session['user_id']
    return redirect(reverse("userLG:login"))


def validateResponse(request,valid,response):
    if valid==False:
        for error in response:
            messages.error(request, error)
        return False

    else:
        return True