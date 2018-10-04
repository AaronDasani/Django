from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Course,Description,Comment
# Create your views here.
def index(request):

    context={
        'course':Course.objects.all(),
    }

    return render(request,'course/index.html',context)


def create(request):

    valid,response=Course.objects.validator(request.POST)

    if valid==False:
        request.session['color']='danger'
        for error in response:
            messages.error(request, error)
        return redirect(reverse('course:index'))

    else:
        request.session['color']='success'
        messages.success(request, "Course successfully created")
        return redirect(reverse('course:index'))


def destroy(request,course_id):
    
    context={
        'course_id':course_id,
        'current_course':Course.objects.get(id=course_id)

    }
    
    return render(request,'course/destroy.html',context)


def delete(request, course_id):
    
    Course.objects.get(id=course_id).delete()


    return redirect(reverse('course:index'))



def comment(request,course_id):
    
    context={
        'course':Course.objects.get(id=course_id),
        'id':course_id,
        'comment':Course.objects.get(id=course_id).comment.all()
    }

    return render(request,'course/comment_page.html',context)


def commentUpdate(request,course_id):
    
    valid,response=Comment.objects.comment_validator(request.POST,course_id)

    if valid==False:
        request.session['color']='danger'
        for error in response:
            messages.error(request, error)
        return redirect(reverse('course:comment',kwargs={'course_id':course_id }))

    else:
        request.session['color']='success'
        messages.success(request, "Course successfully created")
        return redirect(reverse('course:comment',kwargs={'course_id':course_id }))
        
      

   
