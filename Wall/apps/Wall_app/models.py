from __future__ import unicode_literals

from django.db import models
from ..LoginAndReg.models import User
# Create your models here.

class Post(models.Model):
    content=models.TextField()
    user=models.ForeignKey(User,related_name='posts')
    deleteButton=models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    comment=models.TextField()
    post=models.ForeignKey(Post,related_name='comments')
    user=models.ForeignKey(User,related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
