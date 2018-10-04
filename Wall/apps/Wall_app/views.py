from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Post,Comment
from ..LoginAndReg.models import User

# import datetime
from datetime import timedelta,timezone,datetime
import time

def index(request):

    # checking if there a user_id in session
    if 'user_id' not in request.session:
        return redirect(reverse("userLG:login"))

    # getting curent user info
    current_user=User.objects.get(id=request.session['user_id'])

    # checking if to display the delete button in the post
    DeletePost= Post.objects.filter(deleteButton="null")
    for index in DeletePost:
        postTime=index.created_at
        dateNow=datetime.now().replace(tzinfo=timezone(-timedelta(hours=7)))
        minutes_elapsed = (dateNow - postTime).seconds/60

        if minutes_elapsed<30:
            index.deleteButton="display:inline-block"
        else:
            index.deleteButton="display:none"
        index.save()
                
    context={
        'user': current_user,
        'post':Post.objects.order_by("-created_at")
    }
    return render(request,'wall/wall.html',context)

def create(request):
    if 'user_id' not in request.session:
        return redirect(reverse("userLG:login"))

    # post validation
    error=[]
    if len(request.POST['post'])<3:
        error.append("Post should atleast be 3 characters")
        messages.error(request, error)
        return redirect(reverse('wall:index'))
        
    # create the post
    Post.objects.create(content=request.POST['post'],deleteButton="null",user=User.objects.get(id=request.session['user_id']))
    return redirect(reverse('wall:index'))


def createComment(request,post_id):
    if 'user_id' not in request.session:
        return redirect(reverse("userLG:login"))

    # comment validation
    error=[]
    if len(request.POST['comment'])<3:
        error.append("comment should atleast be 3 characters")
        messages.error(request, error)
        return redirect(reverse('wall:index'))

    # create the comment
    Comment.objects.create(comment=request.POST['comment'],post=Post.objects.get(id=post_id), user=User.objects.get(id=request.session['user_id']))
    return redirect(reverse('wall:index'))

def destroy(request,user_id):

    # checking if there is user_id in session
    if 'user_id' not in request.session:
        return redirect(reverse("userLG:login"))

    # checking if the post is for the user and if yes, delete the post
    if request.session['user_id']==int(user_id):
        Post.objects.get(id=request.POST['post_id']).delete()

    return redirect(reverse('wall:index'))