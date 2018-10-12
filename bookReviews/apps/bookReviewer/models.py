from django.db import models

from ..LoginAndRegistration.models import User

# Create your models here.


class BookManager(models.Manager):
    def bookValidator(self,form,user_id):
        error=[]
        # book title
        if len(form['bookTitle'])<1:
            error.append("bookTitle cannot be blank!!")
        if len(form['bookTitle'])<5:
            error.append("First name should be atleat 5 characters")

        # author name
        if len(form["typeAuthor"])<1:
            if len(form["author"])<1:
                error.append("Please provide an author name")
            else:
                author_name=form["author"]
        else:
            if form["author"]:
                error.append("Please include only one Author")
            else:
                if len(form["typeAuthor"])<1:
                    error.append("Please provide an author name")
                elif len(form["typeAuthor"])<5:
                    error.append("author name should be atleast 4 characters")
                else:
                    author_name=form["typeAuthor"]
                    
        # reviews
        if len(form["review"])<1:
            error.append("Please provide a review")
        if len(form["review"])<5:
            error.append("review should be atleast 5 characters")

        # rating
        if len(form["rating"])<1:
            error.append("Please provide a rating")
    
        if error:
            return(False,error)
        else:
            book=Book.objects.create(user=User.objects.get(id=user_id), title=form["bookTitle"],author=author_name)
            Review.objects.create(user=User.objects.get(id=user_id),book=Book.objects.get(id=book.id),review=form["review"],rating=form["rating"])
            return(True,error,book.id)
    
    def AddReviews_validator(self,form,book_id,user_id):
        error=[]
          # reviews
        if len(form["review"])<1:
            error.append("Please provide a review")
        if len(form["review"])<3:
            error.append("review should be atleast 3 characters")

        # rating
        if len(form["rating"])<1:
            error.append("Please provide a rating")
    
        if error:
            return(error)
        else:
            Review.objects.create(user=User.objects.get(id=user_id),book=Book.objects.get(id=book_id),review=form["review"],rating=form["rating"])
            return(error)


class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    objects=BookManager()
    user=models.ForeignKey(User,related_name="book")

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
  
class Review(models.Model):
    review=models.TextField()
    rating=models.IntegerField()
    user=models.ForeignKey(User,related_name="review")
    book=models.ForeignKey(Book,related_name="book_reviews")
    objects=BookManager()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)