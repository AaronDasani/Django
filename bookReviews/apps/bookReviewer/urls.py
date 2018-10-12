from django.conf.urls import url
from .import views


urlpatterns=[
    url(r'^book/$',views.dashboard,name='dashboard'),
    url(r'^create/$',views.create,name='create'),
    url(r'^books/(?P<book_id>\d+)$',views.bookProfile,name='bookProfile'),
    url(r'^users/(?P<user_id>\d+)$',views.userProfile,name='userProfile'),
    url(r'^add_review/(?P<book_id>\d+)$',views.addReview,name='addReview'),
    url(r'^delete_review/(?P<review_id>\d+)/(?P<book_id>\d+)$',views.deleteReview,name='deleteReview')

]