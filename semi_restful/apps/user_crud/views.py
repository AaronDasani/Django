from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
# Create your views here.
from .models import User


def index(request):
    if 'user_id' not in request.session:
        return redirect(reverse('users:new'))

    users=User.objects.all()
    context={
        'users':users
    }
    return render(request,'user_crud/index.html',context)


def new(request):

    return render(request,'user_crud/new.html')


def create(request):
    if request.method!='POST':
        return redirect(reverse('users:new'))
        
    is_valid,response=User.objects.validators(request.POST)

    if is_valid==False:
        for errors in response:
            messages.error(request,errors)
        return redirect(reverse('users:new'))

    request.session['user_id']=response.id
    return redirect(reverse('users:index'))
    



def profile(request,user_id):

    # Ask WES!!!!!
    # print(request.session['user_id'])
    # print(user_id)
    # if user_id != request.session['user_id']:
    #     print('dasd')
    #     return redirect(reverse('users:index'))

    current_user=User.objects.get(id=user_id)
    context={   
        'current_user':current_user
    }


    return render(request, 'user_crud/profile.html',context)


def edit(request,user_id):
    
    return render(request, 'user_crud/edit.html',{'current_user': user_id})
  


def update(request,user_id):

    is_valid,response=User.objects.Update_validators(request.POST,user_id=user_id)

    if is_valid==False:
        for errors in response:
            messages.error(request,errors)

        return redirect(reverse('users:edit', kwargs={'user_id': user_id}))

    return redirect(reverse('users:edit', kwargs={'user_id': user_id}))
  
  
def delete(request,user_id):
    User.objects.get(id=user_id).delete()
    return redirect(reverse('users:index'))