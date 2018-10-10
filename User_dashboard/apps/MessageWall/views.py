from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Post,Comment
from ..LoginAndRegister.models import User

# import datetime
from datetime import timedelta,timezone,datetime
import time

def index(request,currentPage):

    # checking if there a user_id in session
    if 'user_id' not in request.session:
        return redirect(reverse("userLG:login"))

    # getting current user info
    current_user=User.objects.get(id=currentPage)

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
        'post':Post.objects.filter(recipient_id=currentPage).order_by("-created_at")
    }
    return render(request,'message/wall.html',context)

def create(request,currentPage):
    if 'user_id' not in request.session:
        return redirect(reverse("userLG:login"))

    # post validation
    if len(request.POST['post'])<3:
        messages.error(request, "Post should atleast be 3 characters")
        return redirect(reverse('wall:index',kwargs={'currentPage': currentPage }))
        
    # create the post
    Post.objects.create(content=request.POST['post'],location=currentPage,deleteButton="null",recipient=User.objects.get(id=currentPage), user=User.objects.get(id=request.session['user_id']))
    return redirect(reverse('wall:index',kwargs={'currentPage': currentPage }))


def createComment(request,post_id,currentPage):
    if 'user_id' not in request.session:
        return redirect(reverse("userLG:login"))

    # comment validation
    error=[]
    if len(request.POST['comment'])<3:
        error.append("comment should atleast be 3 characters")
        messages.error(request, error)
        return redirect(reverse('wall:index',kwargs={'currentPage': currentPage }))

    # create the comment
    Comment.objects.create(comment=request.POST['comment'],post=Post.objects.get(id=post_id), user=User.objects.get(id=request.session['user_id']))
    return redirect(reverse('wall:index',kwargs={'currentPage': currentPage }))

def destroy(request,user_id,currentPage):

    # checking if there is user_id in session
    if 'user_id' not in request.session:
        return redirect(reverse("userLG:login"))

    # checking if the post is for the user and if yes, delete the post
    if request.session['user_id']==int(user_id):
        Post.objects.get(id=request.POST['post_id']).delete()

    return redirect(reverse('wall:index',kwargs={'currentPage': currentPage }))