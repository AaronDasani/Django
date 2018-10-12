from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Book,Review
from ..LoginAndRegistration.models import User

def dashboard(request):

    if "user_id" not in request.session:
        return redirect(reverse("userLG:login"))

    if "color" not in request.session:
        request.session["color"]="success"
    
    books=Book.objects.all().order_by("-created_at")
    valid_book_list=[]

    for index in books:
       if index.book_reviews.last():
            review=index.book_reviews.last().review
            if len(review)>1:
                valid_book_list.append(index)
          


    context={
        'books':valid_book_list,
        'user':User.objects.get(id=request.session["user_id"]).first_name
    }
    
    return render(request,"bookreviewer/dashboard.html",context)


# create book and reviews
def create(request):
    if request.method == "GET":
        return redirect(reverse("userLG:login"))
    if "user_id" not in request.session:
        return redirect(reverse("userLG:login"))

    valid,response,book_id=Book.objects.bookValidator(request.POST,request.session["user_id"])

    if valid==False:
        request.session["color"]="danger"
        for error in response:
            messages.error(request, error)
    else:
        print("successfully created BOOK")
        request.session["color"]="success"
        messages.success(request, " Book Review Successfully Created")

    return redirect(reverse("books:bookProfile" ,kwargs={'book_id':book_id }))

    



def bookProfile(request,book_id):
    if "user_id" not in request.session:
        return redirect(reverse("userLG:login"))

    context={
        'book':Book.objects.get(id=book_id)
    }

    return render(request,"bookreviewer/book_profile.html",context)



def userProfile(request,user_id):
    try:
        request.session["user_id"]
    except KeyError:
        print("TryAndExcept <<<<<<-------")
        return redirect(reverse("userLG:login"))

    if request.session["user_id"] is not int(user_id):
        print("if <<<<<<-------")
        return redirect(reverse("userLG:login"))

   
    review_list=[]
    for index in Review.objects.raw("SELECT * FROM bookReviewer_review WHERE user_id ="+user_id+"  GROUP BY book_id"):

        review_list.append(index)

    context={
        'user':User.objects.get(id=user_id),
        'book_reviewed':review_list
    }
    
    return render(request,"bookreviewer/user_profile.html",context)
    

def deleteReview(request,review_id,book_id):

    if request.method == "GET":
        return redirect(reverse("userLG:login"))


    Review.objects.get(id=review_id).delete()

    return redirect(reverse("books:bookProfile",kwargs={'book_id':book_id }))

def addReview(request,book_id):
    if request.method == "GET":
        return redirect(reverse("userLG:login"))

    error=Review.objects.AddReviews_validator(form=request.POST,book_id=book_id,user_id=request.session["user_id"])

    if len(error)<1:
        request.session["color"]="danger"
        for error in error:
            messages.error(request, error)

    else:
        request.session["color"]="success"
        messages.success(request, "Review Successfully Created")

    return redirect(reverse("books:bookProfile",kwargs={'book_id':book_id }))