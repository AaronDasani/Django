from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from ..LoginAndRegister.models import User

def Dashboard(request):
    if 'user_id' not in request.session:
        return redirect(reverse("userLG:login"))

    context={
        'all_user':User.objects.all,
        'user':User.objects.get(id=request.session["user_id"])
    }

    # checking if user is an admin or a normal user, and render the appropriate HTML
    if User.objects.get(id=request.session["user_id"]).user_level==0:
        return render(request,"dashboard/UserDashboard.html",context)

    elif User.objects.get(id=request.session["user_id"]).user_level==1:
        return render(request,"dashboard/AdminDashboard.html",context)

def editUser(request,user_id):
    if 'user_id' not in request.session:
        return redirect(reverse("userLG:login"))
    if User.objects.get(id=request.session["user_id"]).user_level==0:
        return redirect(reverse("userLG:login"))
    
    context={
        "user":User.objects.get(id=user_id)    
    }

    return render(request,"dashboard/AdminUserEdit.html",context)




def addUser(request):
    return render(request,"dashboard/newUser.html")



def update(request,user_id):

    valid,response=User.objects.EditUser(request.POST,user_id)

    if valid==False:

        for error in response:
            messages.error(request, error)

        # we can put the hidden value in the modal edit form so we can say if the value in the hidden form is "fromUser" redirect to the profile of the user.
        if request.POST["editRequest"]=="fromUser":
            return redirect(reverse('wall:index',kwargs={'currentPage': user_id }))

        return redirect(reverse("dashboard:editUser",kwargs={'user_id': user_id }))

    # If the FORM values has no errors , we can update the values......
    else:
        EditUser=User.objects.get(id=user_id)

        for key,value in request.POST.items():

            if value=="" or value=="-1" or key=="csrfmiddlewaretoken":
                continue
                
            else:
                if key=="first_name":
                    EditUser.first_name=request.POST[key]
                    EditUser.save()
                elif key=="last_name":
                    EditUser.last_name=request.POST[key]
                    EditUser.save()

                elif key=="email":
                    EditUser.email=request.POST[key]
                    EditUser.save()

                elif key=="user_level":
                    EditUser.user_level=request.POST[key]
                    EditUser.save()

                elif key=="description":
                    EditUser.description=request.POST[key]
                    EditUser.save()
   

    if request.POST["editRequest"]=="fromUser":
        return redirect(reverse('wall:index',kwargs={'currentPage': user_id }))

    return redirect(reverse("dashboard:editUser",kwargs={'user_id': user_id }))


def destroy(request):
    User.objects.get(id=request.POST["user"]).delete()
    return redirect(reverse("dashboard:Dashboard"))


