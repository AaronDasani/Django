from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def validator(self,form):
        error=[]

        if len(form['name'])<5:
            error.append("Course name should be atleast 5 characters")
        if len(form['name'])>40:
            error.append("Course name is too long!!")
        if len(form['desc'])<5:
            error.append("Description should be atleast 5 characters")
        if len(form['desc'])>150:
            error.append("Description is too long!!")
        
        if error:
            return (False,error)
        else:
            c=Course.objects.create(name=form['name'])
            c.save()
            Description.objects.create(desc=form['desc'],course=c)
            return (True,error)
        
    def comment_validator(self,form,course_id):
        error=[]
        if len(form['comment'])<5:
            error.append("Comment should be atleast 5 characters")
        if len(form['comment'])>150:
            error.append("Comment is too long!!")

        if error:
            return (False,error)
        else:
            Comment.objects.create(comment=form['comment'],course_comment=Course.objects.get(id=course_id))
            return (True,error)



class Course(models.Model):
    name=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=CourseManager()

class Description(models.Model):
    desc=models.CharField(max_length=255)
    course=models.OneToOneField(Course,related_name='description')


class Comment(models.Model):
    comment=models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    course_comment=models.ForeignKey(Course,related_name='comment')
    objects=CourseManager()