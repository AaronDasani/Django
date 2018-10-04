from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User
# Create your views here.

def index(request):

    if 'user_id' not in request.session:
        request.session['user_id']=0
    if 'color' not in request.session:
        request.session['color']='danger'

    return render(request,'logAndreg/index.html')

def success(request):
    if 'user_id' not in request.session:
        return redirect(reverse("home:login"))

    
   
    current_user=User.objects.get(id=request.session['user_id'])
    context={
        'user': current_user
    }
    return render(request,'logAndreg/success.html',context)
    
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
        return redirect(reverse("home:success"))
    else:
        return redirect(reverse("home:registration"))
    

def login(request):
    
    return render(request,'logAndreg/login.html')
    
def proccess(request):

    valid,response=User.objects.loginValidation(request.POST)

    if validateResponse(request,valid,response):
        messages.success(request, "Successfully Logged In")
        return redirect(reverse("home:success"))
    else:
        return redirect(reverse("home:login"))
    



def validateResponse(request,valid,response):
    if valid==False:
        request.session['color']='danger'
        for error in response:
            messages.error(request, error)
        return False

    else:
        request.session['color']='success'
        request.session['user_id']=response

        return True