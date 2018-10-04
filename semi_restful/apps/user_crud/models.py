from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
UpperCasePassword_REGEX=re.compile(r'^(?=.*?[A-Z])')
NumericValue_REGEX=re.compile(r'^(?=.*?[0-9])')

class UserManager(models.Manager):
   
    def validators(self,form):
        errors=[]
        #name validation
        if len(form['name'])<1:
            errors.append("First name cannot be blank!!")
        if form['name'].isalpha()==False:
            errors.append("Only letters in the first name")
        if len(form['name'])>20:
            errors.append("First name is too long!!")
        if len(form['name'])<2:
            errors.append("First name should be atleat 2 characters")

        # email validation
        if len(form['email']) < 1:
            errors.append("Email cannot be blank!")
        if not EMAIL_REGEX.match(form['email']):
            errors.append("Invalid Email Address!")

        #password validation
        if len(form['password'])<1:
            errors.append("please provide a password")
        if len(form['password'])<8:
            errors.append("password is too short. Should be atleast 8 characters")
        if not UpperCasePassword_REGEX.match(form['password']) :
            errors.append("at least one uppercase letter")
        if not NumericValue_REGEX.match(form['password']) :
            errors.append("at least one number")

        if errors:
            return(False,errors)
        else:
            User=self.create(name=form['name'],email=form['email'],password=form['password'])
            return (True,User)

    def Update_validators(self,form,user_id):
        errors=[]
        #name validation
        if len(form['name'])<1:
            errors.append("First name cannot be blank!!")
        if form['name'].isalpha()==False:
            errors.append("Only letters in the first name")
        if len(form['name'])>20:
            errors.append("First name is too long!!")
        if len(form['name'])<2:
            errors.append("First name should be atleat 2 characters")

        # email validation
        if len(form['email']) < 1:
            errors.append("Email cannot be blank!")
        if not EMAIL_REGEX.match(form['email']):
            errors.append("Invalid Email Address!")

        if errors:
            return (False,errors)
        else:
            user=self.get(id=user_id)
            user.name=form['name']
            user.email=form['email']
            user.save()
            return (True,errors)







class User(models.Model):
    name = models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=UserManager()